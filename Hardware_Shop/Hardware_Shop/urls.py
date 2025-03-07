# urls.py

from django.contrib import admin
from django.urls import path
from hardware import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('categorie/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorie/<slug:slug>/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('componente/<slug:slug>/detail/', views.componente_detail, name='componente_detail'),
    path('contatti/', views.contatti, name='contatti'),
    ###### UPDATE #######
    path('blog/nuovo/', views.BlogCreateView.as_view(), name='blog-create'),
    path('blog/', views.BlogListView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail')
]
""" Per evitare che Django interpreti erroneamente un URL statico come parte di un URL dinamico, 
    bisogna mettere le rotte più specifiche prima di quelle generiche. 
    In questo caso, blog/nuovo/ è un URL statico, quindi deve essere mappato prima di blog/<slug:slug>/, 
    che è dinamico"""