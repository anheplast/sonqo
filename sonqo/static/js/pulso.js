document.addEventListener('DOMContentLoaded', () => {
    const pulsoContainer = document.getElementById('pulso-container');

    const mostrarDatosPulso = async () => {
        try {
            const response = await fetch('/api/datos_pulso');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();
            console.log('Datos recibidos:', data); // Verifica los datos recibidos en la consola

            // Limpiar contenedor antes de actualizar
            pulsoContainer.innerHTML = '';

            // Mostrar cada dato de pulso recibido
            data.forEach(dato => {
                const pulsoItem = document.createElement('div');
                pulsoItem.classList.add('pulso-item');
                pulsoItem.innerHTML = `<span>Heart Rate:</span> ${dato.heart_rate} bpm<br><span>SPO2:</span> ${dato.spo2}%<br><span>Timestamp:</span> ${dato.timestamp}`;
                pulsoContainer.appendChild(pulsoItem);
            });
        } catch (error) {
            console.error('Error al obtener datos de pulso:', error);
        }
    };

    // Llamar a la función al cargar la página
    mostrarDatosPulso();

    // Actualizar cada 5 segundos (5000 ms)
    setInterval(mostrarDatosPulso, 5000);
});
