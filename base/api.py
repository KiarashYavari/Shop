from base.models import Product
from base.serializers import ProductSerializer
from rest_framework import generics


class CreateProductListApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
