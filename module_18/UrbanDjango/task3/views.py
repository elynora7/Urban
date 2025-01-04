from django.shortcuts import render

# Create your views here.

def games(request):
    games = [
        {'name': 'Atomic Heart'},
        {'name': 'Cyberpunk 2077'},
        {'name': 'PayDay 2'}
    ]
    return render(request, 'games.html', {'games': games})