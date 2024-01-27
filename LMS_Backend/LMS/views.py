from django.shortcuts import render
from .models import User
from .models import Books
from .serializers import UserSerializer
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse


# Create your views here.


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("User added successfully")
        return JsonResponse("Failed to add the user", safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("User is deleted Successfully", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(User, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("User updated successfully")
        return JsonResponse("Failed to update the user", safe=False)


class BooksView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all()


@csrf_exempt
def bookApi(request, id=0):
    if request.method == 'GET':
        books = Books.objects.all()
        books_serializer = BookSerializer(books, many=True)
        return JsonResponse(books_serializer.data, safe=False)
    elif request.method == 'POST':
        books_data = JSONParser().parse(request)
        books_serializer = BookSerializer(data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Book added successfully")
        return JsonResponse("Failed to add the Book", safe=False)
    elif request.method == 'DELETE':
        books = Books.objects.get(id=id)
        books.delete()
        return JsonResponse("Book is deleted Successfully", safe=False)
    elif request.method == 'PUT':
        books_data = JSONParser().parse(request)
        books_serializer = BookSerializer(Books, data=books_data)
        if books_serializer.is_valid():
            books_serializer.save()
            return JsonResponse("Book updated successfully")
        return JsonResponse("Failed to update the Book", safe=False)
