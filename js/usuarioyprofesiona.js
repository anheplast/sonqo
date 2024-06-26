// Este script manejará la visibilidad de las barras de navegación
document.addEventListener("DOMContentLoaded", function () {
    // Asumimos que existe una variable que define si el usuario es profesional de salud o no
    var isProfesionalSalud = false; // Esta variable debe ser configurada según la lógica de tu aplicación

    if (isProfesionalSalud) {
      document.querySelector(".usuario-navbar").style.display = "none";
      document.querySelector(".profesional-navbar").style.display = "block";
    } else {
      document.querySelector(".usuario-navbar").style.display = "block";
      document.querySelector(".profesional-navbar").style.display = "none";
    }
  });