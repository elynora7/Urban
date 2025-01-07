from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import UserRegister
from .models import *


# Create your views here.

def platform(request):
    return render(request, 'platform.html')


def news(request):
    news = News.objects.all().order_by('-date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': page_obj})


def games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            users = Bayer.objects.all()
            errors = []
            if repeat_password != password:
                errors.append('Пароли не совпадают')
            if int(age) < 18:
                errors.append('Вы должны быть старше 18')
            for user in users:
                if user.name == username:
                    errors.append('Пользователь уже существует')
                    break

            if errors:
                info['error'] = ', '.join(errors)
            else:
                Bayer.objects.create(name=username, age=age, balance=0)
                info['text'] = f'Приветствуем, {username}!'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'registration_page.html', info)
