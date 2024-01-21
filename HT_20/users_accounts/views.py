from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse

from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(reverse('products:products_list'))
            else:
                messages.error(request, 'Невірний логін або пароль. Спробуйте ще раз.')

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect(reverse('products:products_list'))
