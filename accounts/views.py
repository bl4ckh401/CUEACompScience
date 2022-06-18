from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CreateUserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response

# Create your views here.


class RegisterUser(APIView):

    def post(self, request, format=None):
        serializer = CreateUserForm(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'User Created'}, status=status.HTTP_200_OK)
        return redirect(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(APIView):

    def post(self, request, format=None):
        serializer = LoginUserForm(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response({'success': 'User Logged In'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'user not found'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogUserOut(APIView):
    def post(request):
        logout(request)
        return redirect('login')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class GetCSRFToken(APIView):
    def get(self, request, format=None):
        return Response({'success': 'CSRF cookie set'})
