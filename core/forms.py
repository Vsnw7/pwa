from django import forms
from .models import MensajeContacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'correo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Tu nombre',
                'class': 'block w-full p-4 rounded mb-3 text-black'
            }),
            'correo': forms.EmailInput(attrs={
                'placeholder': 'Tu correo',
                'class': 'block w-full p-4 rounded mb-3 text-black'
            }),
            'mensaje': forms.Textarea(attrs={
                'placeholder': 'Tu mensaje',
                'class': 'block w-full p-2 rounded mb-3 text-black',
                'rows': 4
            }),
        }

