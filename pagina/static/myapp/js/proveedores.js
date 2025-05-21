// Script para búsqueda de proveedores
document.addEventListener("DOMContentLoaded", function () {
  const searchInput = document.getElementById("searchInput");
  const tableRows = document.querySelectorAll("table tbody tr");

  // Función de búsqueda simplificada
  function filterTable() {
    const searchTerm = searchInput.value.toLowerCase();

    tableRows.forEach((row) => {
      const nit = row.cells[0].textContent.toLowerCase();
      const empresa = row.cells[1].textContent.toLowerCase();
      const correo = row.cells[2].textContent.toLowerCase();
      const telefono = row.cells[3].textContent.toLowerCase();

      // Buscar en todos los campos relevantes
      const matchesSearch =
        nit.includes(searchTerm) ||
        empresa.includes(searchTerm) ||
        correo.includes(searchTerm) ||
        telefono.includes(searchTerm);

      row.style.display = matchesSearch ? "" : "none";
    });
  }

  // Event listeners
  if (searchInput) {
    searchInput.addEventListener("input", filterTable);
  }

  // Botón de reset
  const resetFilters = document.getElementById("resetFilters");
  if (resetFilters) {
    resetFilters.addEventListener("click", () => {
      if (searchInput) {
        searchInput.value = "";
      }
      tableRows.forEach((row) => (row.style.display = ""));
    });
  }

  // Mensaje de depuración
  console.log("Filas encontradas:", tableRows.length);

  // PDF Generation
  const btnGenerarPDF = document.getElementById("btnGenerarPDF");
  if (btnGenerarPDF) {
    btnGenerarPDF.addEventListener("click", function () {
      const { jsPDF } = window.jspdf;
      const doc = new jsPDF();

      // Configurar título
      doc.setFontSize(16);
      doc.text("Listado de Proveedores", 14, 15);
      doc.setFontSize(10);
      doc.text(
        `Fecha de generación: ${new Date().toLocaleDateString()}`,
        14,
        25
      );

      // Preparar datos de la tabla
      const tableData = Array.from(tableRows)
        .filter((row) => row.style.display !== "none")
        .map((row) => [
          row.cells[0].textContent.trim(), // NIT
          row.cells[1].textContent.trim(), // Empresa
          row.cells[2].textContent.trim(), // Correo
          row.cells[3].textContent.trim(), // Teléfono
          row.cells[4].textContent.trim(), // Dirección
          row.cells[5].textContent.trim(), // Fecha
        ]);

      // Generar tabla
      doc.autoTable({
        head: [
          [
            "NIT",
            "Empresa",
            "Correo",
            "Teléfono",
            "Dirección",
            "Fecha Registro",
          ],
        ],
        body: tableData,
        startY: 35,
        theme: "grid",
        styles: {
          fontSize: 8,
          cellPadding: 2,
        },
        headStyles: {
          fillColor: [34, 132, 33],
          textColor: [255, 255, 255],
        },
      });

      // Guardar PDF
      doc.save("listado-proveedores.pdf");
    });
  }
});
