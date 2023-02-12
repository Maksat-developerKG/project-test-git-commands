from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="category", max_length=100)


    class Meta:
        verbose_name = ""
        verbose_name_plural = ""



    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name="name in product:", max_length=100)


    
    class Meta:
        verbose_name = ""
        verbose_name_plural = ""



    def __str__(self) -> str:
        return self.name
