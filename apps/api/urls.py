from django.urls import path
from .views import ReadApiView

app_name = "api"

urlpatterns = [
    path('readapi/', ReadApiView, name='url_read_api'),
]