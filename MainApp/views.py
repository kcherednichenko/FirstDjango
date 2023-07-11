from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    context = {
        'name': 'Ivan',
        'email': 'ivan@mail.ru'
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'name': 'Ivan',
        'surname': 'Ivanov',
        'patronymic': 'Petrovich',
        'phone': '8-923-600-01-02',
        'email': 'vasya@mail.ru'
    }

    return render(request, 'about.html', context)


def item(request, item_id):
    for item_ in items:
        if item_['id'] == item_id:
            context = {
                'item': item_
            }

            return render(request, 'item-page.html', context)

    return HttpResponseNotFound(f"<text>Товар с id = {item_id} не найден</text>")


def items_list(request):
    context = {
        'items': items
    }
    return render(request, 'items-list.html', context)
