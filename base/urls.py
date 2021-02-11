from django.urls import path

from base import views

urlpatterns = [
    path('', views.home),
    # path('^product/<int:product_id>$', 'product')
]
