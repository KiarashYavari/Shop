from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from base.constants import PRODUCTS_PER_PAGE
from base.forms import SignUpForms
from base.models import Product
from django.core.paginator import Paginator


# Create your views here.
@login_required
def home(request):
    products = Product.objects.all()
    paginator = Paginator(products, PRODUCTS_PER_PAGE)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'home.html', {'product_page': page})


class AboutView(TemplateView):
    template_name = 'about.html'


class ProductView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'product.html', {'product': product})


class SignUpView(FormView):
    template_name = 'registration/login.html'
    form_class = SignUpForms
    success_url = reverse_lazy('login')

