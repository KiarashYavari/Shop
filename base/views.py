from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import TemplateView
from base.models import Product


# Create your views here.
def home(request):
    now = datetime.now()
    return render(request, 'home.html', {'now': now})


class AboutView(TemplateView):
    template_name = 'about.html'


class ProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'product.html', {'product': product})
