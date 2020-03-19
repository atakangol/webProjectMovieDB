from django.urls import path
from .views import main

urlpatterns = [
	path('', main, name='url_main'),
    #path('login', views.loginn, name='login'),
    #path('<int:pk>', views.main, name='main')
]
