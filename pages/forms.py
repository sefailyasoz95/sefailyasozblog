from django.forms import ModelForm, TextInput, Textarea

from .models import ContactFormMessage

class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'surname', 'email', 'subject', 'message']
        widgets= {
            'name' : TextInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Your name here'}),
            'surname': TextInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Your surname here'}),
            'email': TextInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Your email here'}),
            'subject': TextInput(attrs={'class': 'form-control border-secondary', 'placeholder': 'Subject'}),
            'message': Textarea(attrs={'class': 'form-control border-secondary', 'placeholder': 'Message', 'rows': '5'}),
        }