function loadPage(page) {
    fetch(page)
        .then(response => response.text())
        .then(data => {
            document.getElementById('main').innerHTML = data;
        })
        .catch(error => {
            console.error('Error al cargar la página:', error);
            document.getElementById('main').innerHTML = '<p>Error al cargar la página.</p>';
        });
}

// Pagina inicial
loadPage('pag1.html');

// Eventos
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        const page = event.target.closest('a').getAttribute('href') + '.html';
        loadPage(page);
    });
});
