from django.urls import path
from django.contrib.auth import views as auth_views
from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>', views.ProductView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('login/', auth_views.LoginView.as_view(), {'template_name': 'templates/login.html'}, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), {'template_name': 'templates/logout.html'}, name='logout'),
]
