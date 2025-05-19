document.addEventListener('DOMContentLoaded', function() {
// Mostrar/ocultar contraseña
const togglePassword = document.querySelector('#togglePassword');
if (togglePassword) {
    const passwordField = document.querySelector('#id_password');
    togglePassword.addEventListener('click', function() {
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    this.querySelector('i').classList.toggle('fa-eye-slash');
    });
}

// Cerrar alertas automáticamente
const alerts = document.querySelectorAll('.alert');
alerts.forEach(alert => {
    setTimeout(() => {
    const bsAlert = new bootstrap.Alert(alert);
    bsAlert.close();
    }, 5000);
});

// Elementos de filtrado
const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const rolFilter = document.getElementById('rolFilter');
const resetFilters = document.getElementById('resetFilters');

// Función para filtrar la tabla
function filterTable() {
    const searchText = searchInput.value.toLowerCase();
    const rolValue = rolFilter.value.toLowerCase();
    const table = document.getElementById('usersTable');
    const rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const cells = row.getElementsByTagName('td');
    if (cells.length === 0) continue;
    
    const username = cells[1].textContent.toLowerCase();
    const document = cells[0].textContent.toLowerCase();
    const rol = cells[4].textContent.toLowerCase();
    
    const textMatch = username.includes(searchText) || document.includes(searchText);
    const rolMatch = rolValue === '' || rol.includes(rolValue);
    
    row.style.display = textMatch && rolMatch ? '' : 'none';
    }
}

// Event listeners para filtros
if (searchInput) {
    searchInput.addEventListener('keyup', filterTable);
}

if (searchButton) {
    searchButton.addEventListener('click', filterTable);
}

if (rolFilter) {
    rolFilter.addEventListener('change', filterTable);
}

if (resetFilters) {
    resetFilters.addEventListener('click', function() {
    searchInput.value = '';
    rolFilter.value = '';
    filterTable();
    });
}

// Sanitización de inputs para prevenir XSS
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', function(e) {
    const inputs = form.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.value = input.value.replace(/</g, '&lt;').replace(/>/g, '&gt;');
    });
    });
});

// Mejorar accesibilidad de tablas en móviles
if (window.innerWidth <= 768) {
    const tableHeaders = document.querySelectorAll('thead th');
    const tableCells = document.querySelectorAll('tbody td');
    
    tableHeaders.forEach((header, index) => {
    const headerText = header.textContent;
    tableCells.forEach(cell => {
        if (cell.cellIndex === index) {
        cell.setAttribute('data-label', headerText);
        }
    });
    });
}

// Animación para contar números en estadísticas
const statsNumbers = document.querySelectorAll('.stats-number');
statsNumbers.forEach(number => {
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
document.getElementById('btnGenerarPDF').addEventListener('click', function() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    
    // Título y fecha
    doc.setFontSize(18);
    doc.text('Listado de Usuarios', 14, 20);
    doc.setFontSize(10);
    const fechaActual = new Date().toLocaleDateString('es-ES');
    doc.text(`Generado el: ${fechaActual}`, 14, 30);
    
    // Información estadística
    doc.setFontSize(12);
    doc.text(`Total usuarios: ${document.querySelector('.stats-number').textContent}`, 14, 40);
    
    // Generar tabla
    doc.autoTable({
    html: '#usersTable',
    startY: 45,
    headStyles: { fillColor: [52, 58, 64] },
    alternateRowStyles: { fillColor: [240, 240, 240] },
    columns: [0, 1, 2, 3, 4, 5], // Excluir la columna de acciones
    columnStyles: {
        0: { cellWidth: 25 }, // Documento
        1: { cellWidth: 30 }, // Usuario
        2: { cellWidth: 20 }, // Tipo Doc
        3: { cellWidth: 40 }, // Correo
        4: { cellWidth: 20 }, // Rol
        5: { cellWidth: 30 }  // Registro
    },
    margin: { top: 45 }
    });
    
    doc.save('listado_usuarios.pdf');
});
});