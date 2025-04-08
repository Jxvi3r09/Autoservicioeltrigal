document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.querySelector("#loginModal form");
  
    if (loginForm) {
      loginForm.addEventListener("submit", function (e) {
        const username = document.getElementById("usuario");
        const password = document.getElementById("contraseña");
  
        // Eliminar alertas anteriores
        const oldAlerts = loginForm.querySelectorAll(".alert");
        oldAlerts.forEach(alert => alert.remove());
  
        // Verificación
        if (username.value.trim() === "" || password.value.trim() === "") {
          e.preventDefault(); // Evita que se envíe el formulario
  
          // Crear y mostrar el mensaje de error
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
  
    // Mostrar / Ocultar contraseña
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
  });
  