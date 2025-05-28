document.addEventListener("DOMContentLoaded", function () {
  const contenedorProductos = document.getElementById("productos-container");
  const btnAgregar = document.getElementById("agregar-producto");
  const formNuevoPedido = document.getElementById("formNuevoPedido");

  // Función para crear nuevo elemento de producto
  function crearProductoItem() {
    const productoTemplate = document
      .querySelector(".producto-item")
      .cloneNode(true);
    productoTemplate.querySelector("select").value = "";
    productoTemplate.querySelector("input").value = "";
    agregarEventoEliminar(productoTemplate.querySelector(".remove-producto"));
    return productoTemplate;
  }

  function agregarEventoEliminar(button) {
    button.addEventListener("click", function () {
      if (document.querySelectorAll(".producto-item").length > 1) {
        Swal.fire({
          title: "¿Está seguro?",
          text: "¿Desea eliminar este producto del pedido?",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Sí, eliminar",
          cancelButtonText: "Cancelar",
        }).then((result) => {
          if (result.isConfirmed) {
            this.closest(".producto-item").remove();
            Swal.fire({
              icon: "success",
              title: "¡Eliminado!",
              text: "El producto ha sido eliminado del pedido.",
            });
          }
        });
      } else {
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Debe mantener al menos un producto en el pedido",
        });
      }
    });
  }

  // Agregar evento al botón de agregar producto
  btnAgregar.addEventListener("click", function () {
    contenedorProductos.appendChild(crearProductoItem());
  });

  // Agregar evento de eliminar al primer elemento
  agregarEventoEliminar(document.querySelector(".remove-producto"));

  // Manejo del formulario de nuevo pedido
  formNuevoPedido.addEventListener("submit", async function (e) {
    e.preventDefault();

    // Validar que haya al menos un producto
    const productos = document.querySelectorAll('select[name="producto[]"]');
    const cantidades = document.querySelectorAll('input[name="cantidad[]"]');
    let isValid = true;

    productos.forEach((producto, index) => {
      if (!producto.value || !cantidades[index].value) {
        isValid = false;
      }
    });

    if (!isValid) {
      Swal.fire({
        icon: "error",
        title: "Error",
        text: "Por favor complete todos los campos del pedido",
      });
      return;
    }

    // Confirmación antes de crear
    const confirmResult = await Swal.fire({
      title: "¿Está seguro?",
      text: "¿Desea crear este nuevo pedido?",
      icon: "question",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Sí, crear",
      cancelButtonText: "Cancelar",
    });

    if (confirmResult.isConfirmed) {
      try {
        const formData = new FormData(this);
        const response = await fetch(this.action, {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          await Swal.fire({
            icon: "success",
            title: "¡Pedido Creado!",
            text: "El pedido se ha creado exitosamente.",
            confirmButtonText: "Aceptar",
            allowOutsideClick: false,
          });
          window.location.reload();
        } else {
          throw new Error("Error en la respuesta del servidor");
        }
      } catch (error) {
        Swal.fire({
          icon: "error",
          title: "Error",
          text: "Hubo un problema al crear el pedido. Por favor, intente nuevamente.",
        });
      }
    }
  });
});
