from django import forms
from .models import Books, Categoey

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title', 
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'rental_per_day',
            'rental_period',
            'total_rent',
            'status',
            'category',
            ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.FileInput(attrs={'class': 'form-control'}),
            'photo_author': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_per_day': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rentprice'}),
            'rental_period': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rentdays'}),
            'total_rent': forms.NumberInput(attrs={'class': 'form-control', 'id': 'renttotal'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            
        }

class CatForm(forms.ModelForm):
    class Meta:
        model = Categoey
        fields = ['name']
        Widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }