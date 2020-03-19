from django.urls import path
from apps.main import views

urlpatterns = [
	path('', views.main, name='main'),
    path('login', views.loginn, name='login'),
    #path('<int:pk>', views.main, name='main')
]
