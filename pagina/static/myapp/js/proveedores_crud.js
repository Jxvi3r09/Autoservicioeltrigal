window.jsPDF = window.jspdf.jsPDF;

// Función para generar PDF
function generarPDF() {
  const doc = new jsPDF("l", "mm", "a4");
  doc.setFontSize(18);
  doc.text("Lista de Proveedores", 15, 15);
  doc.setFontSize(11);
  doc.text(`Fecha: ${new Date().toLocaleDateString()}`, 15, 25);

  const headers = [
    ["NIT", "Empresa", "Correo", "Teléfono", "Dirección", "Fecha Registro"],
  ];
  const data = Array.from(document.querySelectorAll(".table tbody tr"))
    .filter((row) => row.style.display !== "none")
    .map((row) => [
      row.cells[0].textContent.trim(),
      row.cells[1].textContent.trim(),
      row.cells[2].textContent.trim(),
      row.cells[3].textContent.trim(),
      row.cells[4].textContent.trim(),
      row.cells[5].textContent.trim(),
    ]);

  doc.autoTable({
    head: headers,
    body: data,
    startY: 30,
    theme: "grid",
    styles: { fontSize: 8, cellPadding: 2 },
    headStyles: {
      fillColor: [34, 132, 33],
      textColor: 255,
      fontSize: 9,
      fontStyle: "bold",
    },
    columnStyles: {
      0: { cellWidth: 25 },
      1: { cellWidth: 40 },
      2: { cellWidth: 45 },
      3: { cellWidth: 25 },
      4: { cellWidth: 70 },
      5: { cellWidth: 25 },
    },
  });
  doc.save("proveedores.pdf");
}

// Función para mostrar alertas
function showAlert(icon, title, text) {
  Swal.fire({
    icon: icon,
    title: title,
    text: text,
    timer: 5500,
    showConfirmButton: false,
  });
}

// Inicialización cuando el DOM está listo
document.addEventListener("DOMContentLoaded", function () {
  // Botón generar PDF
  const btnPDF = document.getElementById("btnGenerarPDF");
  if (btnPDF) {
    btnPDF.addEventListener("click", generarPDF);
  }

  // Registro de proveedores
  const registerForm = document.querySelector("#registroProveedorModal form");
  if (registerForm) {
    registerForm.addEventListener("submit", function (e) {
      e.preventDefault();
      Swal.fire({
        title: "¿Deseas registrar este proveedor?",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Sí, registrar",
        cancelButtonText: "Cancelar",
      }).then((result) => {
        if (result.isConfirmed) {
          this.submit();
          const modal = bootstrap.Modal.getInstance(
            document.getElementById("registroProveedorModal")
          );
          modal.hide();
          showAlert(
            "success",
            "¡Proveedor registrado!",
            "El proveedor ha sido registrado exitosamente"
          );
        }
      });
    });
  }

  // Edición de proveedores
  document
    .querySelectorAll('[id^="editarProveedorModal"] form')
    .forEach((form) => {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        Swal.fire({
          title: "¿Deseas guardar los cambios?",
          icon: "question",
          showCancelButton: true,
          confirmButtonText: "Sí, guardar",
          cancelButtonText: "Cancelar",
        }).then((result) => {
          if (result.isConfirmed) {
            this.submit();
          }
        });
      });
    });

  // Eliminar proveedores
  document.querySelectorAll(".delete-provider").forEach((button) => {
    button.addEventListener("click", function () {
      const providerId = this.getAttribute("data-id");
      Swal.fire({
        title: "¿Estás seguro?",
        text: "Esta acción no se puede revertir",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar",
        confirmButtonColor: "#d33",
        cancelButtonColor: "#3085d6",
      }).then((result) => {
        if (result.isConfirmed) {
          document.getElementById("deleteForm" + providerId).submit();
        }
      });
    });
  });

  // Verificar mensajes en la URL
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has("success")) {
    showAlert("success", "¡Éxito!", urlParams.get("success"));
  }
  if (urlParams.has("error")) {
    showAlert("error", "Error", urlParams.get("error"));
  }

  // Funcionalidad de búsqueda
  const initializeSearch = () => {
    const searchInput = document.getElementById("searchProvider");
    const tableRows = document.querySelectorAll("table tbody tr");

    const updateEmptyState = (searchTerm) => {
      const visibleRows = document.querySelectorAll(
        'table tbody tr[style=""]'
      ).length;
      const emptyRow = document.querySelector(
        'table tbody tr td[colspan="7"]'
      )?.parentElement;

      if (visibleRows === 0 && !emptyRow) {
        const tbody = document.querySelector("table tbody");
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td colspan="7" class="text-center py-5">
            <i class="fas fa-search fa-3x text-muted mb-3"></i>
            <p class="text-muted">No se encontraron resultados para "${searchTerm}"</p>
          </td>
        `;
        tbody.appendChild(tr);
      } else if (visibleRows > 0 && emptyRow) {
        emptyRow.remove();
      }
    };

    if (searchInput) {
      searchInput.addEventListener("input", function (e) {
        const searchTerm = e.target.value.toLowerCase();

        tableRows.forEach((row) => {
          const text = row.textContent.toLowerCase();
          row.style.display = text.includes(searchTerm) ? "" : "none";
        });

        updateEmptyState(searchTerm);
      });
    }
  };

  // Inicializar búsqueda
  initializeSearch();
});
