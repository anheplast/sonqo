function loadPage(url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById('main').innerHTML = html;
        })
        .catch(error => console.error('Error al cargar la página:', error));
}
