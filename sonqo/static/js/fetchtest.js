// Carga de manera asíncrona en la etiqueta main
function fetchPage(url) {
    fetch(url)
        .then(response => response.text())
        .then(function(data) {
            document.getElementById('main').innerHTML = data;
        })
        .catch(function(error) {
            console.log('Error al cargar contenido:', error);
        });
}



// Paginas -------------------------------------------------------

// Trae la pagina pulso
function fetchPulso() {
    fetchPage('/paginas/pulso');
}

// Trae la pagina consejos
function fetchConsejos() {
    fetchPage('/consejos');
}

// Trae la pagina actividades
function fetchActividades() {
    fetchPage('/actividades');
}

// Trae la pagina playlist
function fetchPlaylist() {
    fetchPage('/playlist');
}

// ---------------------------------------------------------------

// Profesional ---------------------------------------------------

// Trae la pagina de registro para pacientes
function fetchRegistroPacientes() {
    fetchPage('/registro_paciente');
}

// Trae la pagina de la lista pacientes
function fetchListaPacientes() {
    fetchPage('/lista_pacientes');
}

// Trae la pagina listar actividades
function fetchListarActividades() {
    fetchPage('/profesional/listactividades');
}

// Trae la pagina listar consejos
function fetchListarConsejos() {
    fetchPage('/profesional/listconsejos');
}

// Trae la pagina de adminstrador de consejos y actividades
function fetchConsejosActividades() {
    fetchPage('/consejos_actividades');
}

// ---------------------------------------------------------------

// Paginas del Administrador -------------------------------------

// Trae la pagina del admin consejos
function fetchAdminConsejos() {
    fetchPage('/manejar_consejos');
}

// Trae la pagina del admin actividades
function fetchAdminActividades() {
    fetchPage('/manejar_actividades');
}


// Trae la pagina del admin playlist
function fetchAdminPlaylist() {
    fetchPage('/admin/playlist');
}


// ---------------------------------------------------------------
