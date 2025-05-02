 // Script para búsqueda de proveedores
 $(document).ready(function() {
    $("#searchProvider").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("table tbody tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
    
    // Animación de aparición para elementos
    setTimeout(function() {
      $('.fade-in').each(function(i) {
        $(this).css('animation-delay', (i * 0.1) + 's');
      });
    }, 100);
  });