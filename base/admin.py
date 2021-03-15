from django.contrib import admin
from base.models import Product, ProductType


class ProductAdmin(admin.ModelAdmin):
    pass


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

class ProductTypeAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
