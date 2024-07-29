from django import forms
from .models import Game, Comment, compras, Address

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'path', 'description', 'price', 'stocked']
        labels = {
            'title': "Título:",
            'path': "Faça upload:",
            'description': "Descrição:", 
            'price': 'Valor',
            'stocked': 'Quantidade no estoque',         
            }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'path': forms.ClearableFileInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
            'stocked': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': "Comentário:",
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva seu comentario...'}),
        }

class CompraForm(forms.Form):

    class Meta:
        model = compras
        fields = ['quantity']
        labels = {
            'quantity': "Valor Total:",
        }
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade'}),
        }

class AddressForm(forms.ModelForm):
    class Meta: 
        model = Address
        fields = ['rua', 'numero', 'complemento', 'cidade', 'estado', 'cep']
        labels = {
            'rua': "Rua:",
            'numero': "Número:",
            'complemento': "Complemento:",
            'cidade': "Cidade:",
            'estado': "Estado:",
            'cep': "CEP:",
        }
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'form-control mb-3 mt-3 mx-1', 'placeholder': 'Rua'}),
            'numero': forms.TextInput(attrs={'class': 'form-control mb-3 mx-1', 'placeholder': 'Número'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control mb-3 mx-1', 'placeholder': 'Complemento'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control mb-3 mx-1', 'placeholder': 'Cidade'}),
            'estado': forms.TextInput(attrs={'class': 'form-control mb-3 mx-1', 'placeholder': 'Estado'}),
            'cep': forms.TextInput(attrs={'class': 'form-control mb-3 mx-1', 'placeholder': 'CEP'}),
            
        }