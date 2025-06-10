from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product


def basket(request):
    if request.user.is_authenticated:
        basket_ = Basket.objects.filter(user=request.user)
        context = {
            'basket': basket_,
        }
        return render(request, 'basketapp/basket.html, context')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    product_ = get_object_or_404(Product, pk=pk)

    basket_ = Basket.objects.get(user=request.user, product=product_)

    if not basket_:
        basket_ = Basket(user=request.user, product=product_)

    basket_.quantiry += 1
    basket_.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    return render(request, 'basketapp/basket.html')