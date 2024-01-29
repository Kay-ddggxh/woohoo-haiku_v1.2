from django.shortcuts import render
from django.http import HttpResponse


def haikus(request):
    return HttpResponse("Hello Haikus!")
