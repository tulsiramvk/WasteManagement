from django.urls import path
from . import views
app_name='AdminUser'

urlpatterns = [
	path('home/',views.cmpview),
]	