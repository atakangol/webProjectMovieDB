from django.urls import path
from apps.main import views

urlpatterns = [
	path('main', views.main, name='main')
]
