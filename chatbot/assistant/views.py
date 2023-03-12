from django.shortcuts import render
# import HttpResponse from django.urls
from django.http import HttpResponse


# this is the home view for handling home page logic
def home(request):
    return HttpResponse('The Home Page')


# this is the view for handling errors
def error_handler(request):
    return HttpResponse('404 Page')
