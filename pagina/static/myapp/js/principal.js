document.addEventListener("DOMContentLoaded", function () {
  // =============================================
  // Funcionalidad para los mensajes de alerta
  // =============================================
  var alerts = document.querySelectorAll(".alert, #loginModal .alert");

  alerts.forEach(function (alert) {
    // Cierre automático después de 5 segundos
    setTimeout(function () {
      fadeOut(alert);
    }, 5000);

    // Cierre al hacer click en el botón
    var closeBtn = alert.querySelector(".btn-close");
    if (closeBtn) {
      closeBtn.addEventListener("click", function () {
        fadeOut(alert);
      });
    }
  });

  function fadeOut(element) {
    element.style.opacity = "0";
    setTimeout(function () {
      element.style.display = "none";
    }, 500);
  }

  // =============================================
  // Funcionalidad para mostrar/ocultar contraseña
  // =============================================
  function togglePassword() {
    const passwordInput = document.getElementById("contraseña");
    const toggleIcon = document.querySelector("#loginModal .password-toggle i");

    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      toggleIcon.classList.remove("bi-eye-fill");
      toggleIcon.classList.add("bi-eye-slash-fill");
    } else {
      passwordInput.type = "password";
      toggleIcon.classList.remove("bi-eye-slash-fill");
      toggleIcon.classList.add("bi-eye-fill");
    }
  }

  // Asignar el evento al botón de mostrar contraseña
  var passwordToggle = document.querySelector("#loginModal .password-toggle");
  if (passwordToggle) {
    passwordToggle.addEventListener("click", togglePassword);
  }

  // =============================================
  // Validación del formulario de login
  // =============================================
  var loginForm = document.querySelector("#loginModal form");
  if (loginForm) {
    loginForm.addEventListener("submit", function (e) {
      var username = document.getElementById("usuario");
      var password = document.getElementById("contraseña");

      if (username.value.trim() === "" || password.value.trim() === "") {
        e.preventDefault();
        // Mostrar mensaje de error en el modal
        var errorDiv = document.createElement("div");
        errorDiv.className = "alert alert-danger alert-dismissible fade show";
        errorDiv.innerHTML = `
          Por favor complete todos los campos
          <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;

        var modalBody = document.querySelector("#loginModal .modal-body");
        modalBody.insertBefore(errorDiv, modalBody.firstChild);

        // Cerrar automáticamente después de 5 segundos
        setTimeout(function () {
          fadeOut(errorDiv);
        }, 5000);
      }
    });
  }

  // =============================================
  // Mostrar automáticamente el modal si hay errores
  // =============================================

  if (hasErrorMessages) {
    var loginModal = new bootstrap.Modal(document.getElementById("loginModal"));
    loginModal.show();
  }
});


document.addEventListener('DOMContentLoaded', function() {
  // Seleccionamos el carrusel
  const carousel = document.getElementById('customCarousel');
  
  // Configuración del carrusel
  const carouselInstance = new bootstrap.Carousel(carousel, {
    interval: 5000, // Cambia cada 5 segundos
    wrap: true, // Permite bucle infinito
    pause: 'hover' // Pausa al pasar el mouse
  });

  // Opcional: Personalizar la altura del carrusel
  function adjustCarouselHeight() {
    const activeItem = document.querySelector('#customCarousel .carousel-item.active');
    if (activeItem) {
      const img = activeItem.querySelector('img');
      if (img.complete) {
        carousel.style.height = img.height + 'px';
      } else {
        img.onload = function() {
          carousel.style.height = this.height + 'px';
        };
      }
    }
  }

  // Ajustar altura al cargar y al cambiar de slide
  window.addEventListener('load', adjustCarouselHeight);
  carousel.addEventListener('slid.bs.carousel', adjustCarouselHeight);
  
  // Opcional: Ajustar altura al redimensionar la ventana
  window.addEventListener('resize', adjustCarouselHeight);
  
  // Inicializar altura
  adjustCarouselHeight();
  
  // Opcional: Navegación con teclado
  document.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowLeft') {
      carouselInstance.prev();
    } else if (e.key === 'ArrowRight') {
      carouselInstance.next();
    }
  });
});