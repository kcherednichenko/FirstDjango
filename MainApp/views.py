from django.http import HttpResponse

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    text = """<h1>"Изучаем django"</h1> 
    <strong>Автор</strong>: <i>Чередниченко Е.Г.</i>"""

    return HttpResponse(text)


def about(request):
    text = """<text>Имя: Иван<br>
    Отчество: Петрович<br>
    Фамилия: Иванов<br>
    телефон: 8-923-600-01-02<br>
    email: vasya@mail.ru</text>"""

    return HttpResponse(text)


def item(request, item_id):
    text = f"<text>Товар с id = {item_id} не найден</text>"

    for item_ in items:
        if item_id in item_.values():
            text = f"<text>Товар {item_['name']} найден в количестве {item_['quantity']}<text>"
            break

    text += "<p><a href='http://localhost:8000/items/'>Назад к списку товаров</a></p>"

    return HttpResponse(text)


def items_list(request):
    text = """<body>
  <p><strong>Список товаров:</strong></p>
  <ol>
    <li>Кроссовки abibas</li>
    <li>Куртка кожаная</li>
    <li>Coca-cola 1 литр</li>
    <li>Картофель фри</li>
    <li>Кепка</li>
  </ol>
 </body>"""

    return HttpResponse(text)
