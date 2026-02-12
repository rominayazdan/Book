from django.urls import path
from book.views import *


def current_datetime5(request):
    print('request method is', request.method)
    html = 'this is MFT four'
    return html


urlpatterns = [
    path('', home),
    path('index', index),
    path('view', get_all_books),
    path('create', BookAPI.as_view()),
    path('book-generic', BookGenericAPI.as_view()),
    path('book-generic/<int:price>', BookGenericAPI.as_view()),
    path('get-book/<str:price>', GetBookAPI.as_view()),


]
