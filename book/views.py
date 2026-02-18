from dataclasses import fields

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from user.permissions import CustomPermission

from django.template.context_processors import request

from book.models import Book, ImageBook
from django.views.decorators.csrf import csrf_exempt
import json
from book.forms import CreateBook
from rest_framework.views import APIView
from book.serializers import BookSerializer, ImageBookSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

def current_datetime(request):
    print('request method is', request.method)
    now = datetime.datetime.now()
    html = 'this is MFT'
    return HttpResponse(html)


def get_all_books(request):
    books = list(Book.objects.values())

    return JsonResponse(books, safe=False)


def home(request):
    return render(request, 'base.html')


def index(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


@csrf_exempt
def book(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        body['published_date'] = '2026-01-02'
        book = Book.objects.create(**body)
        try:
            return JsonResponse({'book_id': book.id})
        except:
            pass
        return JsonResponse({'error': 'Data format is not correct'})
    elif request.method == "GET":
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)

    elif request.method == "DELETE":
        pass
    elif request.method == "PUT":
        pass


class BookAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        serializer = BookSerializer(data=body)
        if serializer.is_valid():
            book = serializer.save()
            return JsonResponse({'book_id': book.id})
        return JsonResponse({'error': 'Data format is not correct'}, status=400)

    def get(self, request):
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)


class BookGenericAPI(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class GetBookAPI(generics.RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "price"

class BookListAPI(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            user_books = Book.objects.filter(added_by=user)
            published_books = Book.objects.filter(is_published=True)

            return user_books | published_books


        return Book.objects.filter(is_published = True)


class UserListBooksAPI(generics.ListAPIView):
    permission_classes = (AllowAny,CustomPermission)
    serializer_class = BookSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            user_books = Book.objects.filter(added_by=user)
            published_books = Book.objects.filter(is_published=True)

            return user_books | published_books


        return Book.objects.filter(is_published = True)






class AddImageAPI(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ImageBookSerializer

    queryset = ImageBook.objects.all()