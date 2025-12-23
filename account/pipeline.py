from urllib.request import urlopen

from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model

User = get_user_model()

def create_profile(backend, user, response, *args, **kwargs):
    """
    Create a Profile for new users authenticated via social auth.
    Download and save their profile picture from Google.
    """
    from .models import Profile
    
    # Get or create the profile
    profile, created = Profile.objects.get_or_create(user=user)
    
    # If Google auth and profile has no photo, try to get one
    if backend.name == 'google-oauth2':
        # Google provides picture URL in the response
        picture_url = response.get('picture')
        
        if picture_url and not profile.photo:
            try:
                # Download the image
                image_content = urlopen(picture_url).read()
                # Save it to the profile
                profile.photo.save(
                    f'{user.username}_google.jpg',
                    ContentFile(image_content),
                    save=True
                )
            except Exception:
                # If download fails, just continue without photo
                pass




# Optional: Only associate if email is verified (add to pipeline.py)
def associate_by_email_if_verified(backend, details, user=None, *args, **kwargs):
    """
    Only associate by email if the email is verified by the provider.
    """
    if user:
        return None  # User already exists
    
    email = details.get('email')
    if not email:
        return None
    
    # For Google, email is always verified
    if backend.name == 'google-oauth2':
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            existing_user = User.objects.get(email=email)
            return {'user': existing_user}
        except User.DoesNotExist:
            return None
    
    return None