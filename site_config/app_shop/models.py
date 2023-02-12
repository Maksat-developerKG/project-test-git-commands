from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name="Категория:",
        max_length=100,
        blank=True)

    class Meta:
        verbose_name = "Категория:"
        verbose_name_plural = "Категории:"

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField(
        verbose_name="Под категория:",
        max_length=100,
        blank=True)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория:",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Под категория:"
        verbose_name_plural = "Под категории:"

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="Название продукта:", max_length=100)
    description = models.TextField(verbose_name="Описание:")
    img = models.ImageField(
        verbose_name="Изображение:",
        upload_to="media/%Y/%m/%d")
    quantity = models.IntegerField(verbose_name="Количество", default=1)
    price = models.DecimalField(
        verbose_name="Цена:",
        max_digits=10,
        decimal_places=2)
    teh_desc = models.TextField(verbose_name="Техническое описание:")
    pay = models.TextField(verbose_name="Оплата:")
    delivary = models.TextField(verbose_name="Доставка:")
    category = models.ManyToManyField(
        Category, verbose_name="Категория:", blank=True)
    sub_category = models.ManyToManyField(
        SubCategory, verbose_name="Под категория", blank=True)

    class Meta:
        verbose_name = "Продукт:"
        verbose_name_plural = "Продукты:"

    def __str__(self) -> str:
        return self.name
