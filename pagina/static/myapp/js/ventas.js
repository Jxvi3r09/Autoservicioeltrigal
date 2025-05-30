document.addEventListener('DOMContentLoaded', function() {
    const contenedorProductos = document.getElementById('productos-container');

    // Agregar validación antes de enviar el formulario
    document.getElementById('formNuevaVenta').addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Recopilar datos de la tabla
        const productos = [];
        document.querySelectorAll('.producto-item').forEach(row => {
            productos.push({
                id: row.querySelector('input[name="producto[]"]').value,
                cantidad: parseInt(row.querySelector('.cantidad-input').value),
                precio: parseFloat(row.querySelector('.precio-unitario').textContent),
                subtotal: parseFloat(row.querySelector('.subtotal').textContent)
            });
        });

        if (productos.length === 0) {
            alert('Debe agregar al menos un producto');
            return;
        }

        // Preparar datos para envío
        document.getElementById('productos-json').value = JSON.stringify(productos);
        document.getElementById('total-hidden').value = document.getElementById('total-venta').textContent;

        // Enviar formulario
        this.submit();
    });
});


function iniciarEscaneo() {
    const scannerContainer = document.getElementById('scanner-container');
    scannerContainer.style.display = 'block';

    Quagga.init({
        inputStream: {
            name: "Live",
            type: "LiveStream",
            target: document.querySelector("#interactive"),
            constraints: {
                facingMode: "environment",
                width: { min: 640 },
                height: { min: 480 },
                aspectRatio: { min: 1, max: 2 }
            },
            area: {
                top: "0%",
                right: "0%",
                left: "0%",
                bottom: "0%"
            }
        },
        locator: {
            patchSize: "medium",
            halfSample: true
        },
        numOfWorkers: 4,
        decoder: {
            readers: ["ean_reader", "ean_8_reader", "code_128_reader", "code_39_reader", "upc_reader"]
        },
        locate: true
    }, function(err) {
        if (err) {
            console.error("Error al iniciar Quagga:", err);
            alert("Error al iniciar la cámara");
            return;
        }
        console.log("QuaggaJS iniciado correctamente");
        Quagga.start();
    });

    let lastResult = null;
    let countResults = 0;

    

    Quagga.onProcessed(function(result) {
        let drawingCtx = Quagga.canvas.ctx.overlay,
            drawingCanvas = Quagga.canvas.dom.overlay;

        if (result) {
            if (result.boxes) {
                drawingCtx.clearRect(0, 0, parseInt(drawingCanvas.getAttribute("width")), parseInt(drawingCanvas.getAttribute("height")));
                result.boxes.filter(function(box) {
                    return box !== result.box;
                }).forEach(function(box) {
                    Quagga.ImageDebug.drawPath(box, { x: 0, y: 1 }, drawingCtx, { color: "green", lineWidth: 2 });
                });
            }

            if (result.box) {
                Quagga.ImageDebug.drawPath(result.box, { x: 0, y: 1 }, drawingCtx, { color: "#00F", lineWidth: 2 });
            }

            if (result.codeResult && result.codeResult.code) {
                Quagga.ImageDebug.drawPath(result.line, { x: 'x', y: 'y' }, drawingCtx, { color: 'red', lineWidth: 3 });
            }
        }
    });

    Quagga.onDetected(function(result) {
        const code = result.codeResult.code;
        
        if (code === lastResult) {
            countResults++;
            if (countResults >= 3) {
                console.log("Código detectado:", code);
                detenerEscaneo();
                buscarProducto(code);
                lastResult = null;
                countResults = 0;
            }
        } else {
            lastResult = code;
            countResults = 1;
        }
    });
}

function detenerEscaneo() {
    Quagga.stop();
    document.getElementById('scanner-container').style.display = 'none';
}

function buscarProducto(code) {
    console.log("Buscando producto con código:", code);
    fetch(`/buscar-producto/${code}/`)
        .then(response => response.json())
        .then(data => {
            if (data.found) {
                agregarProductoATabla(data, code);
            } else {
                alert('Producto no encontrado');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Error al buscar el producto');
        });
}

function agregarProductoATabla(data, code) {
    const row = document.createElement('tr');
    row.className = 'producto-item';
    const precioUnitario = parseFloat(data.precio).toFixed(2);
    
    row.innerHTML = `
        <td>${code}</td>
        <td>${data.nombre}</td>
        <td>
            <input type="number" class="form-control cantidad-input" 
                   name="cantidad[]" min="1" value="1" max="${data.stock}">
            <input type="hidden" name="producto[]" value="${data.id}">
        </td>
        <td class="precio-unitario">${precioUnitario}</td>
        <td class="subtotal">${precioUnitario}</td>
        <td>
            <button type="button" class="btn btn-danger btn-sm">
                <i class="fas fa-trash"></i>
            </button>
        </td>
    `;
    
    // Agregar la fila a la tabla
    document.getElementById('productos-container').appendChild(row);
    
    // Configurar eventos
    const cantidadInput = row.querySelector('.cantidad-input');
    cantidadInput.addEventListener('input', function() {
        const cantidad = parseInt(this.value) || 0;
        const precio = parseFloat(precioUnitario);
        const subtotal = cantidad * precio;
        row.querySelector('.subtotal').textContent = subtotal.toFixed(2);
        calcularTotal();
    });
    
    row.querySelector('.btn-danger').addEventListener('click', () => {
        row.remove();
        calcularTotal();
    });
    
    // Calcular total inicial
    calcularTotal();
}

function calcularTotal() {
    let total = 0;
    document.querySelectorAll('.subtotal').forEach(cell => {
        const valor = parseFloat(cell.textContent) || 0;
        total += valor;
    });
    document.getElementById('total-venta').textContent = total.toFixed(2);
}

function calcularVueltas() {
    const totalVenta = parseFloat(document.getElementById('total-venta').textContent.replace('$', '').trim());
    
    const montoPago = parseFloat(document.getElementById('monto-pago').value) || 0;
    
    const vueltas = montoPago - totalVenta;
    const vueltasInput = document.getElementById('vueltas');

    if (montoPago < totalVenta) {
        vueltasInput.value = 'Pago insuficiente';
        vueltasInput.style.color = 'red';
        vueltasInput.style.fontWeight = 'bold';
    } else {
        vueltasInput.value = vueltas.toFixed(2);
        vueltasInput.style.color = 'green';
        vueltasInput.style.fontWeight = 'normal';
    }
}