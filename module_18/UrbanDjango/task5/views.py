from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.

users = ['admin', 'user1', 'user2', 'user3']

def sign_up_by_django(request ):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if repeat_password != password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            if not 'error' in info:
                users.append(username)
                info['text'] = f'Приветствуем, {username}!'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)

def sign_up_by_html(request ):
    info = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        age = request.POST['age']
        if repeat_password != password:
            info['error'] = 'Пароли не совпадают'
        if int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        if username in users:
            info['error'] = 'Пользователь уже существует'
        if not 'error' in info:
            users.append(username)
            info['text'] = f'Приветствуем, {username}!'
    return render(request, 'registration_page.html', info)
