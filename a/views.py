from django.shortcuts import render

# Create your views here.

def index(request):
    c = { 'message': 'Welcome',
    }
    return render(request, 'a/index.html', c)
