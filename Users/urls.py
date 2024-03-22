from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserAPIView, 'users')

urlpatterns = [
    # path('', views.UserAPIView, name='Users'),
    path('api/v1/', include(router.urls))
]