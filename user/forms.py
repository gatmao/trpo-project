from django.forms import ValidationError
from django import forms
from .models import CustomUser


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=50, min_length=5)
    email = forms.EmailField(label='Электронная почта')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, min_length=8, max_length=16)
    confirm_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput, min_length=8, max_length=16)

    def clean_username(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username):
            raise ValidationError('Это имя уже занято')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email):
            raise ValidationError('Этот адрес уже используется')
        return email

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['confirm_password']:
            self._errors['password'] = 'Пароли не совпадают'
            self._errors['confirm_password'] = 'Пароли не совпадают'
            del form_data['password']
        return form_data


class PaymentForm(forms.Form):
    payment = forms.IntegerField(label='Сумма', min_value=30)
