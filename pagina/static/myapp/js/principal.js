document.addEventListener("DOMContentLoaded", function () {

  // ======================================================
  // =============== ALERTAS CON AUTO CIERRE ==============
  // ======================================================
  const alerts = document.querySelectorAll(".alert, #loginModal .alert");

  alerts.forEach(function (alert) {
    setTimeout(() => fadeOut(alert), 5000); // Cierre automático

    const closeBtn = alert.querySelector(".btn-close");
    if (closeBtn) {
      closeBtn.addEventListener("click", () => fadeOut(alert));
    }
  });

  function fadeOut(element) {
    element.style.opacity = "0";
    setTimeout(() => element.style.display = "none", 500);
  }

  // ======================================================
  // =========== MOSTRAR MODAL AUTOMÁTICAMENTE ============
  // ======================================================
  if (typeof hasErrorMessages !== "undefined" && hasErrorMessages) {
    const loginModal = new bootstrap.Modal(document.getElementById("loginModal"));
    loginModal.show();
  }

  // ======================================================
  // ================== CARRUSEL AUTOMÁTICO ===============
  // ======================================================
  const carousel = document.getElementById('customCarousel');
  if (carousel) {
    const carouselInstance = new bootstrap.Carousel(carousel, {
      interval: 5000,
      wrap: true,
      pause: 'hover'
    });

    // Ajustar altura del carrusel según la imagen activa
    function adjustCarouselHeight() {
      const activeItem = document.querySelector('#customCarousel .carousel-item.active');
      if (activeItem) {
        const img = activeItem.querySelector('img');
        if (img.complete) {
          carousel.style.height = img.height + 'px';
        } else {
          img.onload = function () {
            carousel.style.height = this.height + 'px';
          };
        }
      }
    }

    window.addEventListener('load', adjustCarouselHeight);
    window.addEventListener('resize', adjustCarouselHeight);
    carousel.addEventListener('slid.bs.carousel', adjustCarouselHeight);
    adjustCarouselHeight();

    // Navegación por teclado
    document.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') {
        carouselInstance.prev();
      } else if (e.key === 'ArrowRight') {
        carouselInstance.next();
      }
    });
  }

});
