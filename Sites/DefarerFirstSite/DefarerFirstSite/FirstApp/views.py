from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import *


def first_page(request):
    return HttpResponse('<p> Привіт із застосунку FirstApp :) </p>')


def old_all_games_view(request):
    all_games = Game.objects.all()
    html = '<ul>'
    for game in all_games:
        html += f'<li>{game}</li>'
    html += '</ul>'
    return HttpResponse(html)


def all_games_view(request):
    all_games = Game.objects.all()

    return render(request, 'all_games.html', context={
        'my_title': 'Всі ігри',
        'games': all_games,
        'min_age': 12
    })
