from django.urls import path
from user.views import *





urlpatterns = [
    path('signup', RegisterUserAPI.as_view()),



]
