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

function fetchConsejos() {
    fetchPage('/consejos');
}

function fetchActividades() {
    fetchPage('/actividades');
}

function fetchPlaylist() {
    fetchPage('/playlist');
}


