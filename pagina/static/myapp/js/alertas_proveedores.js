function confirmarEliminarProveedor(id, empresa) {
  Swal.fire({
    title: "¿Estás seguro?",
    text: `¿Deseas eliminar al proveedor "${empresa}"?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#22B408",
    cancelButtonColor: "#dc3545",
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      const form = document.getElementById(`formEliminar${id}`);
      form.submit();
      Swal.fire({
        title: "¡Eliminado!",
        text: "El proveedor ha sido eliminado correctamente",
        icon: "success",
        confirmButtonColor: "#22B408",
      });
    }
  });
}

// Escuchar el envío del formulario de registro
document.addEventListener("DOMContentLoaded", function () {
  const formRegistro = document.querySelector("#formRegistroProveedor");
  if (formRegistro) {
    formRegistro.addEventListener("submit", function (e) {
      e.preventDefault();
      Swal.fire({
        title: "¡Éxito!",
        text: "Proveedor registrado correctamente",
        icon: "success",
        confirmButtonColor: "#22B408",
      }).then(() => {
        formRegistro.submit();
      });
    });
  }
});

// Función para confirmar edición
function mostrarAlertaEdicion(id, empresa) {
  const modalEditar = $(`#editarProveedorModal${id}`);
  const formEditar = modalEditar.find("form");

  formEditar.on("submit", function (e) {
    e.preventDefault();
    Swal.fire({
      title: "¡Éxito!",
      text: `El proveedor "${empresa}" ha sido actualizado correctamente`,
      icon: "success",
      confirmButtonColor: "#22B408",
    }).then(() => {
      this.submit();
    });
  });

  modalEditar.modal("show");
}
