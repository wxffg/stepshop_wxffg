from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'Главная'

    prods = Product.objects.all()[:3]

    context = {
        'title': title,
        'products': prods,
    }
    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
    }
    return render(request, 'contacts.html', context)
