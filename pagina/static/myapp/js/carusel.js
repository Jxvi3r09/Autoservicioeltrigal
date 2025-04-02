let currentIndex = 0;
    const images = document.querySelectorAll('.carousel-item');
    const totalImages = images.length;

    function moveSlide(direction) {
        currentIndex += direction;
        
        if (currentIndex < 0) {
            currentIndex = totalImages - 1;
        } else if (currentIndex >= totalImages) {
            currentIndex = 0;
        }

        const carouselImages = document.querySelector('.carousel-images');
        carouselImages.style.transform = `translateX(-${currentIndex * 100}%)`;
    }

    setInterval(() => moveSlide(1), 3000);  // Cambio automático de imagen cada 3 segundos