var slideIndex = 0;
showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "inline";
  setTimeout(showSlides, 5000); // Change image every 2 seconds
}



console.log('Hello World')
var categoryLink = document.getElementsByClassName('nav-link');

for (var i = 0; i < categoryLink.length; i++) {
    categoryLink[i].addEventListener("click", function(){
      var categoryId = this.dataset.category
      var action = this.dataset.action
      console.log('categoryId:',categoryId, 'action:',action)
    })
}


