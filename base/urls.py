from django.urls import path

from base import views

urlpatterns = [
    path('', views.home),
    path('product/<int:product_id>', views.ProductView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('signup/', views.signup_form)
]
