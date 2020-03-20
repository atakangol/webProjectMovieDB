from django.urls import path, include
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('register/', register, name='url_register'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='url_login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='url_logout'),
]