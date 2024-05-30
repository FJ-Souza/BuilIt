from django import forms
from django.forms import ModelForm
from .models import AddMaterial

class AddMateriaisForm(forms.ModelForm):
    class Meta:

        model = AddMaterial
        fields = "__all__"
        labels = {
            "path": "img",
            "nome": "Material",
            "valor": "Valor",
        }
        widgets = {
            'path': forms.ClearableFileInput(
                attrs={
                    'placeholder': 'img',
                }
            ),
            'nome': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'gesso',
                }
            ),
            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '10,00',
                }
            )
        }