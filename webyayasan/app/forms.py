from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'id_email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_message'}),
        }
