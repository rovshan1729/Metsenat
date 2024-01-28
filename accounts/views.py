from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated



class UserLogoutView(generics.DestroyAPIView):
        permission_classes = [IsAuthenticated]
        
        def destroy(self, request, *args, **kwargs):
            try:
                request.user.auth_token.delete()
                return Response({'message':'Successfully logged out.'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        



class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

