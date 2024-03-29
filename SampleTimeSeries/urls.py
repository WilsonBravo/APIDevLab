from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_data, name='Sample Time Series Data'),
]