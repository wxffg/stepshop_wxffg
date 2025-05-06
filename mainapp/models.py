from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Имя',
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Катекория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
    )

    name = models.CharField(
        max_length=128,
        verbose_name='Имя продукта',
    )

    image = models.ImageField(
        verbose_name='Изображение',
        blank=True,
        upload_to='product_images',
    )

    short_description = models.CharField(
        max_length=128,
        verbose_name='Краткое описание',
        blank=True,
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )

    price = models.DecimalField(
        verbose_name='Цена',
        default=0,
        max_digits=13,
        decimal_places=2,
    )

    quantity = models.PositiveIntegerField(
        verbose_name='Количество товара',
        default=0,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


