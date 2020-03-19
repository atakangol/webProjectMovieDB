from django.urls import path, include
from apps.users import views as user_v

urlpatterns = [
	path('register/', user_v.register, name='url_register'),
]