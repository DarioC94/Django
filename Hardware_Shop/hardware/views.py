# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Categoria, Componente, BlogPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import django_filters
from .forms import BlogPostForm
# Pagina principale che mostra un'introduzione o un elenco delle categorie
def home(request):
    categorie = Categoria.objects.all()
    return render(request, 'home.html', {'categorie': categorie})

# Vista per la lista delle categorie
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'  # Template per la lista delle categorie
    context_object_name = 'categorie'

# Filtro per i componenti
class ComponenteFilter(django_filters.FilterSet):
    min_prezzo = django_filters.NumberFilter(field_name='prezzo', lookup_expr='gte', label='Min Prezzo')
    max_prezzo = django_filters.NumberFilter(field_name='prezzo', lookup_expr='lte', label='Max Prezzo')
    disponibilita = django_filters.BooleanFilter(field_name='disponibilita', label='Disponibile')

    class Meta:
        model = Componente
        fields = ['min_prezzo', 'max_prezzo', 'disponibilita']

# Vista per i dettagli di una categoria con filtro
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'  # Template per il dettaglio della categoria
    context_object_name = 'categoria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Filtro dei componenti
        categoria = self.get_object()
        componenti = categoria.hardware.all()

        # Applica i filtri
        componenti_filter = ComponenteFilter(self.request.GET, queryset=componenti)
        context['filter'] = componenti_filter
        context['componenti'] = componenti_filter.qs
        return context

# Vista per i dettagli del componente (pagina classica)
class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'componente_detail.html'  # Template per il dettaglio del componente
    context_object_name = 'componente'

def componente_detail(request, slug):
    componente = get_object_or_404(Componente, slug=slug)
    return render(request, 'componente_detail.html', {'componente': componente})


def contatti(request):
    return render(request, 'contatti.html')

############# UPDATE #############

# Vista per la lista degli articoli del blog
class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'articoli'

# Vista per i dettagli di un articolo del blog
class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    context_object_name = 'articolo'

# Vista per la creazione di un nuovo post del blog
class BlogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog_create.html'
    success_url = reverse_lazy('blog-list')

    def form_valid(self, form):
        form.instance.autore = self.request.user  # Assegna l'utente loggato come autore
        return super().form_valid(form)

    def test_func(self):
        # Solo superuser può creare un post
        return self.request.user.is_superuser