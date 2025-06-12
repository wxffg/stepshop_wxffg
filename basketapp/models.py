from django.db import models

class Basket(models.Model):
    @property
    def  product_cost(self):
        return self.product_price * self.quantity

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.quantity, _items)))

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.product_cost, _items)))
