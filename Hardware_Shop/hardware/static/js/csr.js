
      document.addEventListener('DOMContentLoaded', () => {
          // Intercetta i click sui link
          document.querySelectorAll('a').forEach(link => {
              link.addEventListener('click', function (e) {
                  const href = this.getAttribute('href'); // Ottieni l'URL del link
                  // Salta i link che:
                  // 1. Non iniziano con "/"
                  // 2. Contengono "admin" (es. /admin/)
                  if (!href.startsWith('/') || href.includes('admin')) return;
                  e.preventDefault(); // Previeni il comportamento di default
      
                  // Carica il contenuto della nuova pagina
                  fetch(href)
                      .then(response => {
                          if (!response.ok) throw new Error('Errore nel caricamento');
                          return response.text();
                      })
                      .then(html => {
                          // Estrae il blocco #content dalla risposta
                          const parser = new DOMParser();
                          const doc = parser.parseFromString(html, 'text/html');
                          const newContent = doc.querySelector('#content').innerHTML;
      
                          // Sostituisce il contenuto attuale con il nuovo
                          document.querySelector('#content').innerHTML = newContent;
      
                          // Aggiorna l'URL nel browser
                          history.pushState(null, '', href);
                      })
                      .catch(error => {
                          console.error('Errore:', error);
                          alert('Errore durante il caricamento della pagina!');
                      });
              });
          });
      
          // Gestisci la navigazione indietro/avanti
          window.addEventListener('popstate', () => {
              // Ricarica la pagina per assicurare che il contenuto sia aggiornato
              location.reload();
          });
      });
      