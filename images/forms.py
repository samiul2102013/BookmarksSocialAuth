from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from urllib.parse import urlparse, parse_qs
import requests

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }
    
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'webp']
        
        # Parse URL
        parsed_url = urlparse(url)
        path = parsed_url.path
        query = parsed_url.query
        
        # Try to get extension from path
        extension = ''
        if '.' in path:
            try:
                extension = path.rsplit('.', 1)[1].lower()
            except IndexError:
                pass
        
        # If no extension in path, check query parameters (e.g., fm=jpg)
        if not extension or extension not in valid_extensions:
            query_params = parse_qs(query)
            if 'fm' in query_params:
                extension = query_params['fm'][0].lower()
        
        # If still no valid extension, try to detect from content-type
        if not extension or extension not in valid_extensions:
            try:
                response = requests.head(url, timeout=5)
                content_type = response.headers.get('content-type', '')
                if 'jpeg' in content_type or 'jpg' in content_type:
                    extension = 'jpg'
                elif 'png' in content_type:
                    extension = 'png'
                elif 'gif' in content_type:
                    extension = 'gif'
                elif 'webp' in content_type:
                    extension = 'webp'
            except:
                pass
        
        # Accept if we found a valid extension, or if it looks like an image URL
        if extension not in valid_extensions:
            # Last resort: check if URL contains image-related keywords
            url_lower = url.lower()
            if any(ext in url_lower for ext in ['image', 'photo', 'img', 'picture']):
                return url  # Allow it, assume it's an image
            raise forms.ValidationError(
                'The given URL does not match valid image extensions (jpg, jpeg, png, gif, webp).'
            )
        return url
    
    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        
        # Parse URL to get extension
        parsed_url = urlparse(image_url)
        path = parsed_url.path
        query = parsed_url.query
        
        # Try to get extension from path
        extension = ''
        if '.' in path:
            try:
                extension = path.rsplit('.', 1)[1].lower()
            except IndexError:
                pass
        
        # If no extension in path, check query parameters
        if not extension:
            query_params = parse_qs(query)
            if 'fm' in query_params:
                extension = query_params['fm'][0].lower()
        
        # Default to jpg if still no extension
        if not extension:
            extension = 'jpg'
        
        # Convert webp to jpg for compatibility
        if extension == 'webp':
            extension = 'jpg'
        
        image_name = f'{name}.{extension}'
        
        # Download image from the given URL
        response = requests.get(image_url)
        image.image.save(
            image_name,
            ContentFile(response.content),
            save=False
        )
        
        if commit:
            image.save()
        return image