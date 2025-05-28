// Función para mostrar mensajes del backend
function mostrarMensajes(messages) {
  messages.forEach((message) => {
    Swal.fire({
      icon: message.tags === "error" ? "error" : "success",
      title: message.tags === "error" ? "Error" : "¡Éxito!",
      text: message.text,
      confirmButtonColor: message.tags === "error" ? "#dc3545" : "#28a745",
    });
  });
}

// Función para confirmar eliminación
function confirmarEliminacion(id, nombre) {
  const url = `/usuarios/eliminar/${id}/`; // URL construida directamente con el ID
  Swal.fire({
    title: "¿Estás seguro?",
    text: `¿Deseas eliminar al usuario "${nombre}"?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#dc3545",
    cancelButtonColor: "#6c757d",
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      fetch(url, {
        method: "POST",
        headers: {
          "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
            .value,
        },
      })
        .then((response) => {
          if (response.ok) {
            Swal.fire({
              title: "¡Eliminado!",
              text: "El usuario ha sido eliminado correctamente.",
              icon: "success",
              confirmButtonColor: "#28a745",
            }).then(() => {
              window.location.reload();
            });
          } else {
            throw new Error("Error al eliminar el usuario");
          }
        })
        .catch((error) => {
          Swal.fire({
            title: "Error",
            text: error.message,
            icon: "error",
            confirmButtonColor: "#dc3545",
          });
        });
    }
  });
}

// Función para mostrar mensaje después de registrar usuario
function mostrarMensajeRegistro(success = true) {
  Swal.fire({
    title: success ? "¡Usuario Registrado!" : "Error",
    text: success
      ? "El usuario ha sido registrado correctamente."
      : "No se pudo registrar el usuario.",
    icon: success ? "success" : "error",
    confirmButtonColor: success ? "#28a745" : "#dc3545",
  }).then(() => {
    if (success) window.location.reload();
  });
}

// Función para mostrar mensaje después de editar usuario
function mostrarMensajeEdicion(success = true) {
  Swal.fire({
    title: success ? "¡Usuario Actualizado!" : "Error",
    text: success
      ? "El usuario ha sido actualizado correctamente."
      : "No se pudo actualizar el usuario.",
    icon: success ? "success" : "error",
    confirmButtonColor: success ? "#28a745" : "#dc3545",
  }).then(() => {
    if (success) window.location.reload();
  });
}

// Función para confirmar edición
function confirmarEdicion(id, nombre) {
  Swal.fire({
    title: "Editar Usuario",
    text: `¿Deseas editar al usuario "${nombre}"?`,
    icon: "question",
    showCancelButton: true,
    confirmButtonColor: "#ffc107",
    cancelButtonColor: "#6c757d",
    confirmButtonText: "Sí, editar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      const modal = $(`#editarUsuarioModal${id}`);
      modal.modal("show");

      // Agregar listener al formulario de edición
      const form = modal.find("form");
      form.on("submit", function (e) {
        e.preventDefault();
        const formData = new FormData(this);

        fetch(this.action, {
          method: "POST",
          body: formData,
          headers: {
            "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
              .value,
          },
        })
          .then((response) => {
            modal.modal("hide");
            mostrarMensajeEdicion(response.ok);
          })
          .catch(() => mostrarMensajeEdicion(false));
      });
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

function confirmarCerrarSesion(event) {
  event.preventDefault();
  Swal.fire({
    title: "¿Cerrar sesión?",
    text: "¿Estás seguro que deseas cerrar la sesión?",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Sí, cerrar sesión",
    cancelButtonText: "Cancelar",
    allowOutsideClick: false,
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/";
    }
  });
}
