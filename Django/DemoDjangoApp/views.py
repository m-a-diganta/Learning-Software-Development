from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse

# Create your views here.
def home(request):
    context = {
        'line': 'Your sample line here',
        'number': 23.456,
        'list': [3, 2, 7, 4, 5],
    }
    return render(request, 'index.html', context)
def prompt(request):
    return HTTPResponse("This is a prompt page.")
