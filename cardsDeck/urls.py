from django.urls import path
from . import views

urlpatterns = [
    path('', views.cardsDeck, name='cards deck home'),
    path('shuffle/', views.shuffle, name='shuffle cards deck'),
]