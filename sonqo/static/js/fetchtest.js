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

function fetchPulso() {
    fetchPage('/paginas/pulso');
}

function fetchConsejos() {
    fetchPage('/consejos');
}

function fetchActividades() {
    fetchPage('/actividades');
}

function fetchPlaylist() {
    fetchPage('/playlist');
}

function fetchListarActividades() {
    fetchPage('/profesional/listactividades');
}


function fetchListarConsejos() {
    fetchPage('/profesional/listconsejos');
}

function homeUsuario() {
    fetchPage('/usuarios/homeusuario');
}


