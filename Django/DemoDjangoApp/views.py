from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse
from datetime import datetime

# Create your views here.
def home(request):
    context = {
        'line': 'Your sample line here',
        'number': 23.456,
        'list': [3, 2, 7, 4, 5],
        'my_date': datetime.now(),
        'fut_date': datetime(2025, 9, 17),
        'my_string': 'alert("Hello, World!")',
        'my_html': '<h1><b><i>This is a heading</i></b></h1>',
        'cond_var': None,
        'cond_dec': True,
        'dict_list': [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25 }, 
                      {'name': 'Charlie', 'age': 35}],
    }
    return render(request, 'index.html', context)
def prompt(request):
    return HTTPResponse("This is a prompt page.")

def temp_tag(request):
    context = {
        'title': "Let's work with Template Tags now",
        'user': {'name': 'Alfessani', 'is_authenticated': True},
        'products': [{'name': 'Laptop', 'price': 1200},
                    {'name': 'Smartphone', 'price': 800},
                    {'name': 'Tablet', 'price': 600},
                    {'name': 'Smartwatch', 'price': 300},
                    {'name': 'Headphones', 'price': 150}],

    }
    return render(request, 'temp-tag.html', context)
