// =================== PRELOADER ===================
window.addEventListener("load", function () {
    const preloader = document.getElementById("preloader");
    if (preloader) {
      preloader.classList.add("fade-out");
      setTimeout(() => {
        preloader.style.display = "none";
      }, 500); // Tiempo igual al transition en CSS
    }
  });
  
  // =================== INICIALIZACIÓN GENERAL ===================
  document.addEventListener("DOMContentLoaded", function () {
  
    // ========== ALERTAS CON AUTO CIERRE ==========
    const alerts = document.querySelectorAll(".alert, #loginModal .alert");
    alerts.forEach(function (alert) {
      setTimeout(() => fadeOut(alert), 5000);
  
      const closeBtn = alert.querySelector(".btn-close");
      if (closeBtn) {
        closeBtn.addEventListener("click", () => fadeOut(alert));
      }
    });
  
    function fadeOut(element) {
      element.style.opacity = "0";
      setTimeout(() => element.style.display = "none", 500);
    }
  
    // ========== MOSTRAR MODAL AUTOMÁTICAMENTE SI HAY ERRORES ==========
    if (typeof hasErrorMessages !== "undefined" && hasErrorMessages) {
      const loginModal = new bootstrap.Modal(document.getElementById("loginModal"));
      loginModal.show();
    }
  
    // ========== VALIDACIÓN DEL FORMULARIO LOGIN ==========
    const loginForm = document.querySelector("#loginModal form");
    if (loginForm) {
      loginForm.addEventListener("submit", function (e) {
        const username = document.getElementById("usuario");
        const password = document.getElementById("contraseña");
  
        // Eliminar alertas anteriores
        const oldAlerts = loginForm.querySelectorAll(".alert");
        oldAlerts.forEach(alert => alert.remove());
  
        // Verificar campos vacíos
        if (username.value.trim() === "" || password.value.trim() === "") {
          e.preventDefault();
  
          const errorDiv = document.createElement("div");
          errorDiv.className = "alert alert-danger alert-dismissible fade show mt-2";
          errorDiv.innerHTML = `
            Por favor complete todos los campos
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
          `;
  
          const modalBody = document.querySelector("#loginModal .modal-body");
          modalBody.insertBefore(errorDiv, loginForm);
  
          setTimeout(() => {
            errorDiv.classList.remove("show");
            setTimeout(() => errorDiv.remove(), 500);
          }, 5000);
        }
      });
    }
  
    // ========== MOSTRAR / OCULTAR CONTRASEÑA ==========
    const passwordToggle = document.querySelector("#loginModal .password-toggle");
    if (passwordToggle) {
      passwordToggle.addEventListener("click", function () {
        const passwordInput = document.getElementById("contraseña");
        const toggleIcon = passwordToggle.querySelector("i");
  
        if (passwordInput.type === "password") {
          passwordInput.type = "text";
          toggleIcon.classList.replace("bi-eye-fill", "bi-eye-slash-fill");
        } else {
          passwordInput.type = "password";
          toggleIcon.classList.replace("bi-eye-slash-fill", "bi-eye-fill");
        }
      });
    }
  
    // ========== CARRUSEL AUTOMÁTICO ==========
    const carousel = document.getElementById('customCarousel');
    if (carousel) {
      const carouselInstance = new bootstrap.Carousel(carousel, {
        interval: 5000,
        wrap: true,
        pause: 'hover'
      });
  
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
  
      window.addEventListener('resize', adjustCarouselHeight);
      carousel.addEventListener('slid.bs.carousel', adjustCarouselHeight);
      adjustCarouselHeight();
  
      // Navegación con teclado
      document.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowLeft') {
          carouselInstance.prev();
        } else if (e.key === 'ArrowRight') {
          carouselInstance.next();
        }
      });
    }
  
  });
  