from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
#Categoria: cpu, gpu, psu...
class Categoria(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    descrizione = models.TextField()
    immagine = models.URLField(max_length=500)
    slug = models.SlugField() # nome = slug nella url

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"  # Nome plurale personalizzato

    def __str__(self):
        return self.nome

#Componenti: GPU --> rtx 4070, rtx 4060, rtx 4080 etc...    
class Componente(models.Model):
    nome = models.CharField(max_length=120)
    descrizione = models.TextField()
    slug = models.SlugField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='hardware') #si associa a Categoria
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilita = models.BooleanField(default=True)
    data_aggiunta = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True)  # Slug per l'hardware
    immagine = models.URLField(max_length=500) 

    class Meta:
        verbose_name = "Componente"
        verbose_name_plural = "Componenti"  # Nome plurale personalizzato
    def __str__(self):
        return f"{self.categoria.nome}-{self.nome}"
    
########################## UPDATE ######################################
# Blog 
class BlogPost(models.Model):
    titolo = models.CharField(max_length=200)
    contenuto = models.TextField()
    immagine = models.URLField(max_length=500, blank=True, null=True)
    data_pubblicazione = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True) # si leggerà nella URL
    autore = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) #Solo l'admin può creare i blog

    class Meta:
        ordering = ['-data_pubblicazione']

    def __str__(self):
        return self.titolo
    
    def save(self, *args, **kwargs):
        # Impostare lo slug automaticamente solo se non è già presente
        if not self.slug:
            # Usa slugify per generare uno slug a partire dal titolo
            self.slug = slugify(self.titolo)
            
            # Gestione di eventuali slug duplicati
            original_slug = self.slug
            counter = 1
            while BlogPost.objects.filter(slug=self.slug).exists():
                self.slug = f'{original_slug}-{counter}'
                counter += 1

        super().save(*args, **kwargs)