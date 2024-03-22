from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserAPIView, 'users')

urlpatterns = [
    # path('', views.UserAPIView, name='Users'),
    path('api/v1/', include(router.urls)),
    path('users/docs/', include_docs_urls(title="Users API")),
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile),
]