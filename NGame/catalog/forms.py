from django import forms
from .models import Game, Comment

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