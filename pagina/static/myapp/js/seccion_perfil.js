 document.addEventListener('DOMContentLoaded', function() {
    // Previsualizar imagen antes de subir
    const uploadInput = document.getElementById('upload-profile-image');
    const profileImage = document.querySelector('.profile-img');
    
    if (uploadInput && profileImage) {
      uploadInput.addEventListener('change', function() {
        if (this.files && this.files[0]) {
          const reader = new FileReader();
          
          reader.onload = function(e) {
            profileImage.src = e.target.result;
          }
          
          reader.readAsDataURL(this.files[0]);
        }
      });
    }
    
    // Botón de editar perfil
    const editBtn = document.querySelector('.btn-edit-profile');
    if (editBtn) {
      editBtn.addEventListener('click', function() {
        // Aquí se podría implementar la lógica para mostrar un formulario de edición
        alert('Funcionalidad de edición de perfil en desarrollo.');
      });
    }
    
    // Asegurar que la barra lateral permanezca estática
    const body = document.querySelector('body');
    const layout = 'layout-fixed';  // Clase que mantiene el sidebar siempre visible
    
    if (!body.classList.contains(layout)) {
      body.classList.add(layout);
    }
    
    // Ajustar alturas dinámicamente para pantallas pequeñas
    function adjustHeight() {
      const windowHeight = window.innerHeight;
      const sidebar = document.querySelector('.main-sidebar');
      if (sidebar) {
        sidebar.style.height = windowHeight + 'px';
      }
    }
    
    // Ejecutar al cargar y al redimensionar
    adjustHeight();
    window.addEventListener('resize', adjustHeight);
  });