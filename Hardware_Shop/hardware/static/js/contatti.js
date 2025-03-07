document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.querySelector('form');
    const submitButton = contactForm.querySelector('button[type="submit"]');

    contactForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Previeni il comportamento predefinito

        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData.entries()); // Converte i dati in un oggetto

        // Validazione semplice dei campi obbligatori
        if (!data.fullname || !data.email || !data.subject || !data.message) {
            alert();
            return;
        }

        // Validazione dell'email
        if (!validateEmail(data.email)) {
            alert();
            return;
        }

        // Disabilita il bottone mentre invii i dati
        submitButton.disabled = true;
        submitButton.textContent = "Invio in corso...";

        // Simulazione di invio
        setTimeout(() => {
            alert("Messaggio inviato con successo!");
            submitButton.disabled = false;
            submitButton.textContent = "Invio Messaggio";
            contactForm.reset(); // Resetta il modulo
        }, 5000); // Simula un'attesa di 2 secondi
    });

    // Funzione per validare l'email
    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }
});
