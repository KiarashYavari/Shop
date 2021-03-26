import factory
from factory.django import DjangoModelFactory


class ProductTypeFactory(DjangoModelFactory):
    class Meta:
        model = 'ProductType'
        django_get_or_create = ('title',)


class ProductListFactory(DjangoModelFactory):
    class Meta:
        model = 'Product'
        django_get_or_create = ('Name', 'Price', 'Type',)

