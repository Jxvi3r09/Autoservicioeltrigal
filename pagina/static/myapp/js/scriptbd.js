// Mostrar fecha actual
const currentDate = new Date();
const options = { year: "numeric", month: "long", day: "numeric" };
document.getElementById("current-date-display").textContent =
  currentDate.toLocaleDateString("es-ES", options);

// Toggle sidebar en móviles
const sidebarToggler = document.getElementById("sidebarToggler");
sidebarToggler.addEventListener("click", () => {
  document.body.classList.toggle("sidebar-open");
});
