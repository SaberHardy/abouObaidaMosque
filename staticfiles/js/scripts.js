function initializeSlideshow() {
    var imgs = document.querySelectorAll('.header img');
    var dots = document.querySelectorAll('.dot');
    var currentImg = 0;
    const interval = 2000;

    var timer = setInterval(changeSlide, interval)

    function changeSlide(n) {
        for (var i = 0; i < imgs.length; i++) {
            imgs[i].style.opacity = 0;
            dots[i].className = dots[i].className.replace(' active-dot', '');
        }
        currentImg = (currentImg + 1) % imgs.length;
        if (n !== undefined) {
            clearInterval(timer);
            timer = setInterval(changeSlide, interval);
            currentImg = n;
        }

        imgs[currentImg].style.opacity = 1;
        dots[currentImg].className += ' active-dot';
    }
}


// Call all functions
document.addEventListener('DOMContentLoaded', function () {
    initializeSlideshow();
});