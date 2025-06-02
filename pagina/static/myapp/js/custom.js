document.addEventListener("DOMContentLoaded", function() {
    const buttonLabels = {
        "Readable Font": "Fuente Legible",
        "Highlight Links": "Resaltar Enlaces",
        "Highlight Title": "Resaltar Título",
        "Monochrome": "Monocromo",
        "Low Saturation": "Baja Saturación",
        "High Saturation": "Alta Saturación",
        "High Contrast": "Alto Contraste",
        "Light Contrast": "Bajo Contraste",
        "Dark Contrast": "Contraste Oscuro",
        "Big Cursor": "Cursor Grande",
        "Stop Animations": "Detener Animaciones",
        "Reading Guide": "Guía de Lectura"
    };

    document.querySelectorAll('.asw-btn').forEach(button => {
        const key = button.querySelector('.material-icons').nextSibling.nodeValue.trim();
        if (buttonLabels[key]) {
            button.querySelector('.material-icons').nextSibling.nodeValue = buttonLabels[key];
        }
    });
});

      function descargarManual() {
        const link = document.createElement('a');
        link.href = "/media/manuales/manual_usuario.pdf";
        link.download = 'manual_usuario.pdf';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }