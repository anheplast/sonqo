document.getElementById('registroForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const formData = new FormData(this);
    const formDataObj = Object.fromEntries(formData.entries());
    console.log(formDataObj);


});
