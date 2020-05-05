from ckeditor.widgets import CKEditorWidget
from django import forms
from django.forms import ModelForm
from .models import Blog


class NewBlog(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'blog': forms.Textarea(),
        }

class ReadingCount(ModelForm):
    class Meta:
        model = Blog
        fields = []