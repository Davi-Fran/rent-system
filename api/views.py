from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

@api_view(["GET", "POST"])
def user_route(request):
    if request.method == "GET":
        queryset = User.objects.all().order_by("username")
        serializers = UserSerializer(queryset, many=True)

        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializers = UserSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            return Response(serializers.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)


class UsersRouteAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetailAPIView(APIView):
    def get_object(self, pk):
        return User.objects.get(pk=pk)


    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)


    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)