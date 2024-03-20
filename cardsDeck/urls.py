from django.urls import path
from .views import *

urlpatterns = [
    path('', cardsDeck, name='cards deck home'),
]