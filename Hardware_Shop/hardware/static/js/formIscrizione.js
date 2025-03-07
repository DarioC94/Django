//FORM DI REGISTRAZIONE
// Funzione per alternare la visibilità della password
const togglePassword = document.getElementById('togglePassword');
const password = document.getElementById('password');
togglePassword.addEventListener('click', function (e) {
    // Cambia il tipo dell'input tra password e text
    const type = password.type === 'password' ? 'text' : 'password';
    password.type = type;
    // Cambia l'icona (attiva/disattiva l'icona dell'occhio)
    this.classList.toggle('fa-eye-slash');
});

// Funzione per alternare la visibilità della conferma della password
const toggleConfirmPassword = document.getElementById('toggleConfirmPassword');
const confirmPassword = document.getElementById('confirmPassword');
toggleConfirmPassword.addEventListener('click', function (e) {
    // Cambia il tipo dell'input tra password e text
    const type = confirmPassword.type === 'password' ? 'text' : 'password';
    confirmPassword.type = type;
    // Cambia l'icona (attiva/disattiva l'icona dell'occhio)
    this.classList.toggle('fa-eye-slash');
});



function validazione() {
    let valido = true;

    // Validazione Nome
    const name = document.getElementById('name');
    const erroreName = document.getElementById('erroreName');
    if (name.value.trim() === "") {
        valido = false;
        mostraErrore(name, erroreName, "Il campo Nome è obbligatorio.");
    } else {
        nascondiErrore(name, erroreName);
    }

    // Validazione Cognome
    const lastName = document.getElementById('lastName');
    const erroreLastName = document.getElementById('erroreLastName');
    if (lastName.value.trim() === "") {
        valido = false;
        mostraErrore(lastName, erroreLastName, "Il campo Cognome è obbligatorio.");
    } else {
        nascondiErrore(lastName, erroreLastName);
    }

    // Validazione Email
    const email = document.getElementById('email');
    const erroreEmail = document.getElementById('erroreEmail');
    const regexEmail = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!regexEmail.test(email.value)) {
        valido = false;
        mostraErrore(email, erroreEmail, "Inserire un'email valida.");
    } else {
        nascondiErrore(email, erroreEmail);
    }

    // Validazione Password
    const password = document.getElementById('password');
    const errorePassword = document.getElementById('errorePassword');
    const regexPassword = /^(?=.*[A-Z])(?=.*[0-9])(?=.*[\W_]).{6,}$/;
    if (!regexPassword.test(password.value)) {
        valido = false;
        mostraErrore(password, errorePassword, "La password deve contenere almeno una maiuscola, un numero e un simbolo speciale.");
    } else {
        nascondiErrore(password, errorePassword);
    }

    // Validazione Conferma Password
    const confirmPassword = document.getElementById('confirmPassword');
    const erroreConfirmPassword = document.getElementById('erroreConfirmPassword');
    if (password.value !== confirmPassword.value) {
        valido = false;
        mostraErrore(confirmPassword, erroreConfirmPassword, "Le password non coincidono.");
    } else {
        nascondiErrore(confirmPassword, erroreConfirmPassword);
    }

    // Se tutti i campi sono validi, mostra un alert di conferma
    if (valido) {
        const name = document.getElementById('name').value; // Recupera il nome inserito
        alert(`Registrazione completata con successo, ${name}! Ora sei dei nostri!`);
        document.getElementById('formRegistrazione').submit();  // Invia il form
    }

}

function mostraErrore(campo, spanErrore, messaggio) {
    campo.classList.add('input-errore');
    spanErrore.textContent = messaggio;
}

function nascondiErrore(campo, spanErrore) {
    campo.classList.remove('input-errore');
    spanErrore.textContent = '';
}

// Rimozione dell'errore quando l'utente modifica l'input
document.getElementById('name').addEventListener('input', () => nascondiErrore(name, erroreName));
document.getElementById('lastName').addEventListener('input', () => nascondiErrore(lastName, erroreLastName));
document.getElementById('email').addEventListener('input', () => nascondiErrore(email, erroreEmail));
document.getElementById('password').addEventListener('input', () => nascondiErrore(password, errorePassword));
document.getElementById('confirmPassword').addEventListener('input', () => nascondiErrore(confirmPassword, erroreConfirmPassword));
