from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from book.models import Book
from django.views.decorators.csrf import csrf_exempt
import json
from book.forms import CreateBook
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework import generics


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
    elif request.method == "DELETE":
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)

    elif request.method == "DELETE":
        pass
    elif request.method == "PUT":
        pass


class BookAPI(APIView):

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

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class GetBookAPI(generics.RetrieveDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "price"
