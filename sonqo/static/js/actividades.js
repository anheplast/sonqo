document.addEventListener('DOMContentLoaded', function() {
    var buttons = document.querySelectorAll('.ver-mas-btn');

    buttons.forEach(function(button) {
        button.addEventListener('click', function() {
            var fullText = this.nextElementSibling;
            if (fullText.style.display === 'none' || fullText.style.display === '') {
                fullText.style.display = 'block';
                this.textContent = 'Ver menos';
            } else {
                fullText.style.display = 'none';
                this.textContent = 'Ver más';
            }
        });
    });
});
