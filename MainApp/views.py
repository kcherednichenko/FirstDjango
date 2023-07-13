from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item


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
    try:
        item_ = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"<text>Товар с id = {item_id} не найден</text>")
    else:
        item_colours = []
        for colour in item_.colours.all():
            item_colours.append(colour.name)

        context = {
            'item': item_,
            'colours': item_colours
        }

        return render(request, 'item-page.html', context)


def items_list(request):
    items = Item.objects.all()

    context = {
        'items': items
    }
    return render(request, 'items-list.html', context)
