from rest_framework import viewsets, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .serializer import *
from .models import *

class UserAPIView(viewsets.ModelViewSet):
    serializer_class = profileSerializer
    queryset = User.objects.all()

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update(request):
    if 'username' not in request.data:
        return Response({"error": "You need to provide an username to perform this action."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user = get_object_or_404(User, username=request.data["username"])
        if user.is_staff:
            return Response({"error":"You do not have permissions to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        del(request.data["username"])

    serializer = UserSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        for value in request.data:
            setattr(user, value, request.data[value])
            user.save()
        return Response({"OK":1}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete(request):
    if 'username' not in request.data:
        return Response({"error": "You need to provide an username to perform this action."}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user = get_object_or_404(User, username=request.data["username"])
        if user.is_staff:
            return Response({"error":"You do not have permissions to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        
        user.delete()
        return Response({"OK":1}, status=status.HTTP_200_OK)

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data["username"])
    if not user.check_password(request.data['password']):
        return Response({"error":"Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = loginUserSerializer(instance=user)

    return Response({"token":token.key,"user":serializer.data},status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        if "email" not in request.data:
            return Response({
                        "email": [
                            "This field is required."
                        ]
                    }, status=status.HTTP_400_BAD_REQUEST)
        else:
            if User.objects.filter(
                email=serializer.data["email"]
            ).exists():
                return Response({
                    "email": [
                        "An user with that email already exists."
                    ]
                }, status=status.HTTP_400_BAD_REQUEST)
          
        user = User.objects.create(
            username=serializer.data["username"],
            first_name=serializer.data["first_name"],
            last_name=serializer.data["last_name"],
            email=serializer.data["email"],

        )

        user.set_password(serializer.data["password"])
        user.save()

        customFields.objects.create(
            user=user,
            birthdate=serializer.data["custom_fields"]["birthdate"],
            gender=serializer.data["custom_fields"]["gender"],
        ).save()
        
        token = Token.objects.create(user=user)
        return Response({
                'token': token.key,
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        
    # Conditional errors
    errors = serializer.errors
    
    if "email" not in request.data:
        errors["email"] = ["This field is required."]
    else:
        if User.objects.filter(
            email=serializer.data["email"]
        ).exists():
            errors["email"] = ["An user with that email already exists."]

    return Response(errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user=User.objects.get(username=request.user.username)
    serializer = profileSerializer(instance=user)

    return Response({"user": serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
def get_users(request):
    users=User.objects.all()
    serializer = profileSerializer(users, many=True)

    return Response({"users": serializer.data}, status=status.HTTP_200_OK)