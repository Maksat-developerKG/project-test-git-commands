from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name="category", max_length=100)


    class Meta:
        verboser_name = ""
        verboser_name_plural = ""

        

    def __str__(self) -> str:
        return self.name