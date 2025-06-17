from basketapp.models import Basket


def get_main_menu(current='mainapp:index'):
    return [
        {'href': 'mainapp:index', 'name': 'Главная', 'active': current},
        {'href': 'mainapp:products', 'name': 'Товары', 'active': current},
        {'href': 'mainapp:about', 'name': 'О нас', 'active': current},
        {'href': 'mainapp:contacts', 'name': 'Контакты', 'active': current},
    ]


def get_basket(user=None):
    if user and user.is_authenticated:
        return Basket.objects.filter(user=user)
    return None