from django.urls import path
from apps.main import views

urlpatterns = [
	path('', views.main, name='main'),
    path('register', views.register, name='register'),
    path('login', views.loginn, name='login'),
    #path('<int:pk>', views.main, name='main')
]
