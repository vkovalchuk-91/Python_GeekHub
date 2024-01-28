from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Логін', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
