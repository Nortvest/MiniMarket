from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import *


class AddProductForm(forms.ModelForm):
    """Форма добавления нового товара в таблицу ProductsModel"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = ProductsModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Как называется ваш товар?'}),
            'description': forms.Textarea(attrs={'cols': 60,
                                                 'rows': 5,
                                                 'class': 'form-control',
                                                 'placeholder': 'Напишите описание к товару'}),
            'photo': forms.FileInput(attrs={'accept': ".jpg, .jpeg, .png", 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control',
                                              'placeholder': 'Укажите цену за продукт'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price


class AddUserForm(UserCreationForm):
    photo = forms.ImageField(label='Аватар',
                             widget=forms.FileInput(attrs={'accept': ".jpg, .jpeg, .png", 'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Придумайте пароль'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Повторите пароль'}))

    class Meta:
        model = UsersModel
        fields = ('username', 'first_name', 'last_name', 'email', 'photo')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кажите ваше имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите вашу фамилию'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Придумайте UserName'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите вашу электронную почту'})
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Ник',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите UserName'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Придумайте пароль'}))
