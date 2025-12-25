const siteUrl = 'https://127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250;
const minHeight = 250;

// Load CSS
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random()*9999999999999999);
head.appendChild(link);

// Load HTML
var body = document.getElementsByTagName('body')[0];
var boxHtml = `
  <div id="bookmarklet">
    <a href="#" id="bookmarklet-close">&times;</a>
    <h1>Select an image to bookmark:</h1>
    <div class="images"></div>
  </div>`;
body.innerHTML += boxHtml;

function myBookmarklet() {
  var bookmarklet = document.getElementById('bookmarklet');
  var imagesFound = bookmarklet.querySelector('.images');
  
  // Clear images found
  imagesFound.innerHTML = '';
  // Display bookmarklet
  bookmarklet.style.display = 'block';
  
  // Close event
  bookmarklet.querySelector('#bookmarklet-close')
             .addEventListener('click', function(){
    bookmarklet.style.display = 'none';
  });
  
  // Find ALL images on the page (not just specific extensions)
  var images = document.querySelectorAll('img');
  images.forEach(image => {
    // Check if image has valid src and meets minimum size
    if(image.src && image.naturalWidth >= minWidth && image.naturalHeight >= minHeight) {
      var imageFound = document.createElement('img');
      imageFound.src = image.src;
      imagesFound.appendChild(imageFound);
    }
  });
  
  // Select image event
  imagesFound.querySelectorAll('img').forEach(image => {
    image.addEventListener('click', function(e){
      var imageSelected = e.target.src;
      bookmarklet.style.display = 'none';
      window.open(siteUrl + 'images/create/?url='
                  + encodeURIComponent(imageSelected)
                  + '&title='
                  + encodeURIComponent(document.title),
                  '_blank');
    });
  });
}

// Run the bookmarklet
myBookmarklet();