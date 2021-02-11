from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from base.models import Product


# Create your views here.
def home(request):
    now = datetime.now()
    return HttpResponse('<html><body>Hello World! time:{}</body></html>'.format(now))


class ProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=None)
        return
