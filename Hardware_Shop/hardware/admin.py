from django.contrib import admin

# Register your models here.

from .models import BlogPost, Categoria, Componente

class CategoriaAdmin(admin.ModelAdmin):
    # Popola automaticamente il campo slug
    prepopulated_fields = {"slug": ("nome",)}
    # Mostra questi campi nell'elenco delle categorie
    list_display = ('nome', 'descrizione', 'slug')
    # Permette la ricerca per nome
    search_fields = ('nome',)
    # Aggiungi filtri per le categorie
    list_filter = ('nome',) 


class ComponenteAdmin(admin.ModelAdmin):
    # Popola automaticamente il campo slug
    prepopulated_fields = {"slug": ("nome",)}
    # Mostra questi campi nell'elenco dei componenti
    list_display = ('nome', 'categoria', 'prezzo', 'disponibilita', 'data_aggiunta')
    # Permette la ricerca per nome e categoria
    search_fields = ('nome', 'categoria__nome')
    # Aggiungi filtri per disponibilità e categoria
    list_filter = ('disponibilita', 'categoria')

######### UPDATE #########
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'autore', 'data_pubblicazione', 'slug')  # Visualizza titolo, autore, data pubblicazione e slug
    search_fields = ('titolo', 'autore__username')  # Permette la ricerca per titolo e autore
    prepopulated_fields = {'slug': ('titolo',)}  # Genera automaticamente lo slug dal titolo



# Registrazione dei modelli nell'admin
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Componente, ComponenteAdmin)
admin.site.site_header = "Amministrazione Hardware Store"
admin.site.site_title = "Admin Hardware Store"
admin.site.index_title = "Admin Hardware Store"
admin.site.register(BlogPost, BlogPostAdmin)