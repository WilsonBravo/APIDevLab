from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import AutoSchema
from rest_framework import routers
from . import views


urlpatterns = [
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile),
    re_path('update', views.update),
    re_path('delete', views.delete),
    re_path('users', views.get_users),
    # path('', views.UserAPIView, name='Users'),
    # path('api/v1/', include(router.urls)),
    # path('users/docs/', include_docs_urls(title="Users API", schema_url='/api/v1/schema')),
]
# router = routers.DefaultRouter()
# router.register(r'users', views.UserAPIView, 'users')