from django.shortcuts import render

# this is the home view for handling home page logic
def home(request):
    return render(request, 'assistant/home.html')

# this is the view for handling errors
def error_handler(request):
    return render(request, 'assistant/404.html')
