from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category
from mainapp.utils import get_main_menu, get_basket


def index(request):
    title = 'Главная'

    temp = 'Мы крутая команда'

    prods = Product.objects.all()[:4]

    context = {
        'temp': temp,
        'title': title,
        'products': prods,
        'basket': get_basket(request.user),
        'menu_links': get_main_menu(),
    }

    return render(request, 'index.html', context)

def contacts(request):
    title = 'Контакты'
    temp = 'У нас лучшая группа'
    context = {
        'temp': temp,
        'title': title,
        'basket': get_basket(request.user),
        'menu_links': get_main_menu('mainapp:contacts'),
    }
    return render(request, 'contacts.html', context)

def about(request):
    title = 'О нас'
    context = {
        'title': title,
        'basket': get_basket(request.user),
        'menu_links': get_main_menu('mainapp:about'),
    }
    return render(request, 'about.html', context)

def products(request, pk=None):
    title = 'Товары'
    prods = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'title': title,
        'products': prods,
        'categories': categories,
        'menu_links': get_main_menu('mainapp:products'),
        'basket': get_basket(request.user),
    }

    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products_ = Product.objects.filter(category__pk=pk)

        context.update({'products': products_, 'category': category})


    return render(request, 'products.html', context)

def product(request, pk):
    title = 'Товар'

    prod = Product.objects.get(id=pk)
    same_prods = Product.objects.exclude(id=pk)

    context = {
        'title': title,
        'product': prod,
        'products': same_prods,
        'basket': get_basket(request.user),
        'menu_links': get_main_menu('mainapp:products'),
    }
    return render(request, 'product.html', context)


