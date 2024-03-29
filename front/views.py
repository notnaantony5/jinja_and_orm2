import datetime

from django.shortcuts import render


def index(request):
    posts = [
        {
            'author': 'Вася Васечкин',
            'title': 'Пост 1',
            'date': datetime.date(2020,
                                  3, 12),
            'text': 'Случайный текст случайный текст '
                    'случайный текст случайный текст '
                    'случайный текст случайный текст '
        },
        {
            'author': 'Петя Петичкин',
            'title': 'Пост лучший 2',
            'date': datetime.date(2022,
                                  6, 1),
            'text': 'Случайный текст2 случайный текст '
                    'случайный текст случайный текст2 '
                    'случайный текст2 случайный текст '
        }
    ]
    return render(request,
                  'index.html',
                  {'title': 'Главная',
                   'posts': posts})
