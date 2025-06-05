from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, Category


def get_main_menu(current='mainapp:index'):
     return [
        {'href': 'mainapp:index', 'name': 'Главная', 'active': 'mainapp:current'},
        {'href': 'mainapp:products', 'name': 'Товары', 'active': 'mainapp:current'},
        {'href': 'mainapp:about', 'name': 'О нас', 'active': 'mainapp:current'},
        {'href': 'mainapp:contacts', 'name': 'Контакты', 'active': 'mainapp:current'},
]


def index(request):
    title = 'Главная'

    prods = Product.objects.all()[:4]

    context = {
        'title': title,
        'products': prods,
        'menu_links': get_main_menu(),
    }
    return render(request, 'index.html', context)


def about(request):
    title = 'О нас'

    context = {
        'title': title,
        'about': about,
        'menu_links': get_main_menu('mainapp:about'),

    }
    return render(request, 'about.html', context)


def contacts(request):
    title = 'Контакты'

    context = {
        'title': title,
        'menu_links': get_main_menu('mainapp:contacts'),

    }
    return render(request, 'contacts.html', context)


def products(request, pk=None):
    title = 'Товары'
    prods = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'title': title,
        'products': prods,
        'categories': categories,
        'menu_links': get_main_menu('mainapp:products'),
    }
    
    if pk is not None:
        if pk == 0:
            products_ = Product.objects.all()
            category = {'name': 'все'}
        else:
            category = get_object_or_404(Category, pk=pk)
            products_ = Product.objects.filter(categoty__pk=pk)
            
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
        'menu_links': get_main_menu('mainapp:products'),

    }
    return render(request, 'product.html', context)
