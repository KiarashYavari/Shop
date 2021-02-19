from django.contrib.auth.models import AbstractUser
from django.db import models


class ProductType(models.Model):
    title = models.CharField(verbose_name="عنوان", max_length=128)

    def __str__(self):
        return self.title


class Product(models.Model):
    Price = models.IntegerField(verbose_name="قیمت", default=0)
    Name = models.CharField(verbose_name="اسم", max_length=128)
    Type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Name', 'Type')


class Members(AbstractUser):
    pass
