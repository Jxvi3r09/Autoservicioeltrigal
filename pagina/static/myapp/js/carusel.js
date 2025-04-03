let currentIndex = 0;
    const images = document.querySelectorAll('.imagenes img');
    const totalImages = images.length;

    function mostrarSiguienteImagen() {
        index++;
        if (index >= totalImages) {
            index = 0; // Volver al principio cuando llegue al final
        }
    
        // Mover el carrusel a la imagen correspondiente
        document.querySelector('.imagenes').style.transform = `translateX(-${index * 100}%)`;
    }
    
    // Cambiar imagen cada 3 segundos
    setInterval(mostrarSiguienteImagen, 3000);
        
        