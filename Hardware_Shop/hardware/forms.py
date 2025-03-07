from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['titolo', 'contenuto', 'immagine']
        widgets = {
            'titolo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenuto': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'immagine': forms.URLInput(attrs={'class': 'form-control'}),
        }
