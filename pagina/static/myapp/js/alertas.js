// Función para mostrar mensajes del backend
function mostrarMensajes(messages) {
    messages.forEach(message => {
        Swal.fire({
            icon: message.tags === "error" ? 'error' : 'success',
            title: message.tags === "error" ? 'Error' : '¡Éxito!',
            text: message.text,
            confirmButtonColor: message.tags === "error" ? '#dc3545' : '#28a745'
        });
    });
}

// Función para confirmar eliminación
function confirmarEliminacion(id, nombre) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: `¿Deseas eliminar al usuario "${nombre}"?`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#dc3545',
        cancelButtonColor: '#6c757d',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            document.getElementById(`formEliminar${id}`).submit();
        }
    });
}

// Función para confirmar edición
function confirmarEdicion(id, nombre) {
    Swal.fire({
        title: 'Editar Usuario',
        text: `¿Deseas editar al usuario "${nombre}"?`,
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#ffc107',
        cancelButtonColor: '#6c757d',
        confirmButtonText: 'Sí, editar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            $(`#editarUsuarioModal${id}`).modal('show');
        }
    });
}

// // Inicialización de eventos
// document.addEventListener('DOMContentLoaded', function() {
//     // Confirmación para nuevo usuario
//     const btnNuevoUsuario = document.querySelector('button[data-bs-target="#registroModal"]');
//     if (btnNuevoUsuario) {
//         btnNuevoUsuario.addEventListener('click', function(e) {
//             e.preventDefault();
//             Swal.fire({
//                 title: 'Nuevo Usuario',
//                 text: '¿Deseas registrar un nuevo usuario?',
//                 icon: 'question',
//                 showCancelButton: true,
//                 confirmButtonColor: '#28a745',
//                 cancelButtonColor: '#6c757d',
//                 confirmButtonText: 'Sí, continuar',
//                 cancelButtonText: 'Cancelar'
//             }).then((result) => {
//                 if (result.isConfirmed) {
//                     $('#registroModal').modal('show');
//                 }
//             });
//         });
//     }
// });
