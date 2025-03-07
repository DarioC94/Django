//MODAL DELLA COMPONENTE SPECIFICA
document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".btn-info");
    const modal = document.getElementById("componentModal");
    const modalContent = document.getElementById("modalContent");
    const closeModalBtn = document.querySelector(".modal-close");

    // Funzione per aprire il modal e caricare i dettagli
    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const slug = button.getAttribute("data-slug");
            fetch(`/componente/${slug}/detail/`)
                .then(response => {
                    if (!response.ok) throw new Error("Errore nella risposta del server");
                    return response.text();
                })
                .then(data => {
                    modalContent.innerHTML = data;
                    modal.classList.add("show");
                })
                .catch(error => console.error("Errore nel caricamento del dettaglio:", error));
        });
    });

    // Chiudi il modal cliccando sulla "X"
    closeModalBtn.addEventListener("click", function () {
        modal.classList.remove("show");
    });

    // Chiudi il modal cliccando fuori dal contenuto del modal
    modal.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.classList.remove("show");
        }
    });
});
