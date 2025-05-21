function confirmarEliminarProveedor(id, empresa) {
  Swal.fire({
    title: "¿Estás seguro?",
    text: `¿Deseas eliminar al proveedor "${empresa}"? Esta acción eliminará también todos los pedidos asociados.`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#d33",
    cancelButtonColor: "#3085d6",
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      document.getElementById(`formEliminar${id}`).submit();
    }
  });
}

function mostrarAlertaEdicion(id, empresa) {
  const modalEditar = document.querySelector(`#editarProveedorModal${id}`);
  const form = modalEditar.querySelector("form");

  // Mostrar el modal
  const modal = new bootstrap.Modal(modalEditar);
  modal.show();

  // Manejar el envío del formulario
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    Swal.fire({
      title: "¿Guardar cambios?",
      text: `¿Deseas actualizar los datos del proveedor "${empresa}"?`,
      icon: "question",
      showCancelButton: true,
      confirmButtonColor: "#22B408",
      cancelButtonColor: "#d33",
      confirmButtonText: "Sí, actualizar",
      cancelButtonText: "Cancelar",
    }).then((result) => {
      if (result.isConfirmed) {
        form.submit();
      }
    });
  });
}
