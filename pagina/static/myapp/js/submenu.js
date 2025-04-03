$(document).ready(function () {
  $(".nav-item > a").on("click", function (e) {
    var $this = $(this);

    if ($this.next(".nav-treeview").length) {
      e.preventDefault();

      $this.next(".nav-treeview").slideToggle();

      $this.find(".right").toggleClass("fa-angle-left fa-angle-down");
    }
  });
});


<script>
  document.addEventListener('DOMContentLoaded', function() {
    const btnAbrirModal = document.getElementById('btnAbrirModal');
    const modalRegistro = document.getElementById('modalRegistro');
    const btnCerrarModal = document.getElementById('btnCerrarModal');

    // Función para abrir el modal
    btnAbrirModal.addEventListener('click', function() {
      modalRegistro.style.display = 'block';
      modalRegistro.setAttribute('aria-hidden', 'false');
    });

    // Función para cerrar el modal al hacer clic en la X
    btnCerrarModal.addEventListener('click', function() {
      modalRegistro.style.display = 'none';
      modalRegistro.setAttribute('aria-hidden', 'true');
    });

    // Cerrar el modal al hacer clic fuera del contenido
    window.addEventListener('click', function(event) {
      if (event.target === modalRegistro) {
        modalRegistro.style.display = 'none';
        modalRegistro.setAttribute('aria-hidden', 'true');
      }
    });
  });
</script>
