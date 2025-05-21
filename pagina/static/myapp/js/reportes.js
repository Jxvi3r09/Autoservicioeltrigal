document.addEventListener("DOMContentLoaded", function () {
  // Mostrar/ocultar contraseña
  const togglePassword = document.querySelector("#togglePassword");
  if (togglePassword) {
    const passwordField = document.querySelector("#id_password");
    togglePassword.addEventListener("click", function () {
      const type =
        passwordField.getAttribute("type") === "password" ? "text" : "password";
      passwordField.setAttribute("type", type);
      this.querySelector("i").classList.toggle("fa-eye-slash");
    });
  }

  // Cerrar alertas automáticamente
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach((alert) => {
    setTimeout(() => {
      const bsAlert = new bootstrap.Alert(alert);
      bsAlert.close();
    }, 5000);
  });

  // Elementos de filtrado
  const searchInput = document.getElementById("searchInput");
  const searchButton = document.getElementById("searchButton");
  const rolFilter = document.getElementById("rolFilter");
  const resetFilters = document.getElementById("resetFilters");

  // Función para filtrar la tabla
  function filterTable() {
    const searchText = searchInput.value.toLowerCase();
    const rolValue = rolFilter.value.toLowerCase();
    const table = document.getElementById("usersTable");
    const rows = table.getElementsByTagName("tr");

    for (let i = 1; i < rows.length; i++) {
      const row = rows[i];
      const cells = row.getElementsByTagName("td");
      if (cells.length === 0) continue;

      const username = cells[1].textContent.toLowerCase();
      const document = cells[0].textContent.toLowerCase();
      const rol = cells[4].textContent.toLowerCase();

      const textMatch =
        username.includes(searchText) || document.includes(searchText);
      const rolMatch = rolValue === "" || rol.includes(rolValue);

      row.style.display = textMatch && rolMatch ? "" : "none";
    }
  }

  // Event listeners para filtros
  if (searchInput) {
    searchInput.addEventListener("keyup", filterTable);
  }

  if (searchButton) {
    searchButton.addEventListener("click", filterTable);
  }

  if (rolFilter) {
    rolFilter.addEventListener("change", filterTable);
  }

  if (resetFilters) {
    resetFilters.addEventListener("click", function () {
      searchInput.value = "";
      rolFilter.value = "";
      filterTable();
    });
  }

  // Sanitización de inputs para prevenir XSS
  const forms = document.querySelectorAll("form");
  forms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      const inputs = form.querySelectorAll("input, textarea");
      inputs.forEach((input) => {
        input.value = input.value.replace(/</g, "&lt;").replace(/>/g, "&gt;");
      });
    });
  });

  // Mejorar accesibilidad de tablas en móviles
  if (window.innerWidth <= 768) {
    const tableHeaders = document.querySelectorAll("thead th");
    const tableCells = document.querySelectorAll("tbody td");

    tableHeaders.forEach((header, index) => {
      const headerText = header.textContent;
      tableCells.forEach((cell) => {
        if (cell.cellIndex === index) {
          cell.setAttribute("data-label", headerText);
        }
      });
    });
  }

  // Animación para contar números en estadísticas
  const statsNumbers = document.querySelectorAll(".stats-number");
  statsNumbers.forEach((number) => {
    const finalValue = parseInt(number.textContent);
    let currentValue = 0;
    const duration = 1500;
    const increment = finalValue / (duration / 16);

    function updateCounter() {
      if (currentValue < finalValue) {
        currentValue += increment;
        number.textContent = Math.ceil(currentValue);
        requestAnimationFrame(updateCounter);
      } else {
        number.textContent = finalValue;
      }
    }

    updateCounter();
  });

  // Exportar a PDF
  document
    .getElementById("btnGenerarPDF")
    .addEventListener("click", function () {
      const { jsPDF } = window.jspdf;
      const doc = new jsPDF();

      // Configurar título
      doc.setFontSize(16);
      doc.text("Listado de Usuarios", 14, 15);
      doc.setFontSize(10);
      doc.text(
        `Fecha de generación: ${new Date().toLocaleDateString()}`,
        14,
        25
      );

      // Obtener datos de la tabla
      const tableRows = document.querySelectorAll("#usersTable tbody tr");
      const tableData = Array.from(tableRows)
        .filter((row) => row.style.display !== "none")
        .map((row) => [
          row.cells[0].textContent.trim(), // Documento
          row.cells[1].textContent.trim(), // Usuario
          row.cells[2].textContent.trim(), // Tipo Doc
          row.cells[3].textContent.trim(), // Correo
          row.cells[4].textContent.trim(), // Rol
          row.cells[5].textContent.trim(), // Registro
        ]);

      // Generar tabla con los colores de proveedores
      doc.autoTable({
        head: [
          ["Documento", "Usuario", "Tipo Doc.", "Correo", "Rol", "Registro"],
        ],
        body: tableData,
        startY: 35,
        theme: "grid",
        styles: {
          fontSize: 8,
          cellPadding: 2,
        },
        headStyles: {
          fillColor: [34, 132, 33], // Color verde de proveedores
          textColor: [255, 255, 255],
        },
        alternateRowStyles: {
          fillColor: [245, 245, 245],
        },
      });

      doc.save("listado-usuarios.pdf");
    });
});
