// Obtener elementos del DOM
const addProductBtn = document.getElementById('addProductBtn');
const addCategoryBtn = document.getElementById('addCategoryBtn');
const addProductModal = document.getElementById('addProductModal');
const addCategoryModal = document.getElementById('addCategoryModal');
const editCategoryModal = document.getElementById('editCategoryModal');
const editProductModal = document.getElementById('editProductModal');
const closeModalBtns = document.querySelectorAll('.close-modal');
const cancelAddProduct = document.getElementById('cancelAddProduct');
const cancelAddCategory = document.getElementById('cancelAddCategory');
const addCategoryForm = document.getElementById('addCategoryForm');
const editCategoryForm = document.getElementById('editCategoryForm');
const editProductForm = document.getElementById('editProductForm');

// Mostrar modales
addProductBtn.addEventListener('click', () => {
    addProductModal.style.display = 'block';
});

addCategoryBtn.addEventListener('click', () => {
    addCategoryModal.style.display = 'block';
});

// Ocultar modales con botones de cancelar y cerrar
cancelAddProduct.addEventListener('click', () => {
    addProductModal.style.display = 'none';
});

cancelAddCategory.addEventListener('click', () => {
    addCategoryModal.style.display = 'none';
});

closeModalBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        addProductModal.style.display = 'none';
        addCategoryModal.style.display = 'none';
        editCategoryModal.style.display = 'none';
        editProductModal.style.display = 'none';
    });
});

// Cerrar modal al hacer clic fuera
window.addEventListener('click', (event) => {
    if (event.target === addProductModal) {
        addProductModal.style.display = 'none';
    }
    if (event.target === addCategoryModal) {
        addCategoryModal.style.display = 'none';
    }
    if (event.target === editCategoryModal) {
        editCategoryModal.style.display = 'none';
    }
    if (event.target === editProductModal) {
        editProductModal.style.display = 'none';
    }
});

// Enviar formulario para agregar categoría
addCategoryForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(addCategoryForm);

    fetch('/agregar-categoria/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            addCategoryModal.style.display = 'none';
            addCategoryForm.reset();
            Swal.fire({
                icon: 'success',
                title: 'Categoría guardada correctamente',
                confirmButtonText: 'Aceptar'
            }).then(() => location.reload());
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: data.error || 'Error al agregar la categoría'
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        Swal.fire({
            icon: 'error',
            title: 'Error inesperado',
            text: 'No se pudo completar la solicitud'
        });
    });
});

// Funciones para editar y eliminar categorías, productos, filtros, etc.
// ... (el resto de tu código permanece igual sin modificaciones en esta parte)



function eliminarCategoria(id) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: 'Esta acción eliminará la categoría permanentemente.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(`/eliminar-categoria/${id}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    Swal.fire(
                        'Eliminado',
                        'La categoría ha sido eliminada correctamente.',
                        'success'
                    ).then(() => location.reload());
                } else {
                    Swal.fire(
                        'Error',
                        data.error || 'No se pudo eliminar la categoría.',
                        'error'
                    );
                }
            })
            .catch(error => {
                console.error('Error:', error);
                Swal.fire(
                    'Error',
                    'Ocurrió un error inesperado.',
                    'error'
                );
            });
        }
    });
}

function editarCategoria(id, nombre) {
    document.getElementById('edit_categoria_id').value = id;
    document.getElementById('edit_categoria_nombre').value = nombre;
    document.getElementById('editCategoryModal').style.display = 'block';
}

document.getElementById('editCategoryForm').addEventListener('submit', (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);
    const categoriaId = formData.get('categoria_id');

    fetch(`/editar-categoria/${categoriaId}/`, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            Swal.fire({
                icon: 'success',
                title: 'Categoría actualizada correctamente',
                confirmButtonText: 'Aceptar'
            }).then(() => location.reload());
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: data.error || 'No se pudo editar la categoría'
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
        Swal.fire({
            icon: 'error',
            title: 'Error inesperado',
            text: 'Ocurrió un problema al editar la categoría'
        });
    });
});


        function eliminarProducto(id) {
            Swal.fire({
                title: '¿Estás seguro?',
                text: "No podrás revertir esta acción",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, eliminar',
                cancelButtonText: 'Cancelar'
            }).then((result) => {
                if (result.isConfirmed) {
                    fetch(`/eliminar_producto/${id}/`, {
                        method: 'POST',
                        headers: {
                            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success) {
                            Swal.fire(
                                '¡Eliminado!',
                                'El producto ha sido eliminado.',
                                'success'
                            ).then(() => {
                                location.reload();
                            });
                        } else {
                            Swal.fire(
                                'Error',
                                data.error || 'Error al eliminar el producto',
                                'error'
                            );
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        Swal.fire(
                            'Error',
                            'Error al eliminar el producto',
                            'error'
                        );
                    });
                }
            });
        }

        function filtrarPorCategoria(categoriaId) {
            // Remover clase active de todas las categorías
            document.querySelectorAll('.category-item').forEach(item => {
                item.classList.remove('active');
            });
            // Agregar clase active a la categoría seleccionada
            if (categoriaId === 'todas') {
                document.getElementById('categoria-todas').classList.add('active');
            } else {
                document.getElementById(`categoria-${categoriaId}`).classList.add('active');
            }
            // Filtrar productos
            const productos = document.querySelectorAll('.product-card');
            productos.forEach(producto => {
                if (categoriaId === 'todas') {
                    producto.style.display = 'block';
                } else {
                    const productoCategoriaId = producto.getAttribute('data-categoria');
                    producto.style.display = productoCategoriaId === categoriaId ? 'block' : 'none';
                }
            });
        }

        // Activar "Todas las categorías" por defecto
        document.addEventListener('DOMContentLoaded', () => {
            document.getElementById('categoria-todas').classList.add('active');
        });

        function buscarProductos() {
            const searchText = document.getElementById('searchInput').value.toLowerCase();
            const productos = document.querySelectorAll('.product-card');
            let found = false;
            productos.forEach(producto => {
                const nombre = producto.querySelector('.product-title').textContent.toLowerCase();
                const categoria = producto.querySelector('.product-category').textContent.toLowerCase();
                const codigo = producto.querySelector('.spec-label + span').textContent.toLowerCase();
                if (nombre.includes(searchText) || 
                    categoria.includes(searchText) || 
                    codigo.includes(searchText)) {
                    producto.style.display = 'block';
                    found = true;
                } else {
                    producto.style.display = 'none';
                }
            });
            // Mostrar mensaje si no hay resultados
            const noProducts = document.querySelector('.no-products');
            if (!found && !noProducts) {
                const message = document.createElement('div');
                message.className = 'no-products';
                message.innerHTML = '<p>No se encontraron productos</p>';
                document.querySelector('.product-grid').appendChild(message);
            } else if (found && noProducts) {
                noProducts.remove();
            }
        }

        function ordenarProductos() {
            const sortBy = document.getElementById('sortSelect').value;
            const productos = Array.from(document.querySelectorAll('.product-card'));
            productos.sort((a, b) => {
                switch(sortBy) {
                    case 'precio-asc':
                        return getPrecio(a) - getPrecio(b);
                    case 'precio-desc':
                        return getPrecio(b) - getPrecio(a);
                    case 'nombre-asc':
                        return getNombre(a).localeCompare(getNombre(b));
                    case 'nombre-desc':
                        return getNombre(b).localeCompare(getNombre(a));
                    default:
                        return 0;
                }
            });
            const container = document.querySelector('.product-grid');
            productos.forEach(producto => container.appendChild(producto));
        }

        function limitarProductos() {
            const limit = parseInt(document.getElementById('limitSelect').value);
            const productos = document.querySelectorAll('.product-card');
            productos.forEach((producto, index) => {
                producto.style.display = index < limit ? 'block' : 'none';
            });
        }

        function getPrecio(producto) {
            return parseFloat(producto.querySelector('.product-price').textContent.replace('$', ''));
        }

        function getNombre(producto) {
            return producto.querySelector('.product-title').textContent;
        }

        // Inicializar los filtros
        document.addEventListener('DOMContentLoaded', () => {
            ordenarProductos();
            limitarProductos();
        });

        function editarProducto(id) {
            console.log('Editando producto:', id);
            fetch(`/productos/obtener/${id}/`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error al obtener producto');
                    }
                    return response.json();
                })
                .then(producto => {
                    console.log('Producto recibido:', producto);
                    document.getElementById('edit_producto_id').value = producto.id;
                    document.getElementById('edit_producto_barcode').value = producto.id; // Agregar esta línea
                    document.getElementById('edit_producto_nombre').value = producto.nombre;
                    document.getElementById('edit_producto_categoria').value = producto.categoria;
                    document.getElementById('edit_producto_precio').value = producto.precio;
                    document.getElementById('edit_producto_cantidad_producto').value = producto.cantidad_producto;
                    
                    const editProductModal = document.getElementById('editProductModal');
                    editProductModal.style.display = 'block';
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error al cargar el producto: ' + error.message);
                });
        }

        document.getElementById('editProductForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const productoId = formData.get('producto_id');
            // Si hay imagen nueva y está recortada
            if (cropper && document.querySelector('[name="imagen"]').files.length > 0) {
                cropper.getCroppedCanvas().toBlob((blob) => {
                    formData.delete('imagen');
                    formData.append('imagen', blob, 'cropped.jpg');
                    enviarFormularioEdicion(formData, productoId);
                });
            } else {
                enviarFormularioEdicion(formData, productoId);
            }
        });

        function enviarFormularioEdicion(formData, productoId) {
            fetch(`/productos/editar/${productoId}/`, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Error en la respuesta del servidor');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    location.reload();
                } else {
                    alert('Error al editar el producto: ' + (data.error || 'Error desconocido'));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error al editar el producto');
            });
        }

            function closeEditProductModal() {
                document.getElementById('editCategoryModal').style.display = 'none';
            }


        let cropper = null;
    
        function previewImage(input) {
            const preview = document.getElementById('imagePreview');
            const file = input.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    preview.style.display = 'block';
                    if (cropper) {
                        cropper.destroy();
                    }
                    cropper = new Cropper(preview, {
                        aspectRatio: NaN, // Permite cualquier relación de aspecto
                        viewMode: 2,
                        dragMode: 'move',
                        autoCropArea: 0.8,
                        restore: false,
                        guides: true,
                        center: true,
                        highlight: false,
                        cropBoxMovable: true,
                        cropBoxResizable: true,
                        toggleDragModeOnDblclick: true,
                        zoomable: true,
                        zoomOnWheel: true,
                        scalable: true,
                        rotatable: true
                    });
                }
                reader.readAsDataURL(file);
            }
        }

        // Funciones para controlar el cropper
        function zoomIn() {
            if (cropper) cropper.zoom(0.1);
        }

        function zoomOut() {
            if (cropper) cropper.zoom(-0.1);
        }

        function rotateLeft() {
            if (cropper) cropper.rotate(-90);
        }

        function rotateRight() {
            if (cropper) cropper.rotate(90);
        }

        function resetCrop() {
            if (cropper) cropper.reset();
        }