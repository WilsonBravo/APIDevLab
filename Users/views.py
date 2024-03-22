from rest_framework import viewsets
from .serializer import *
from .models import *

class UserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()