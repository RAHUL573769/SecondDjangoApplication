from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("This is my firsdt Page")


def about(request):
    return HttpResponse("This is About")
