from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'saludo': 'hola django'
    }
    return render(request, 'myapp/index.html', context)
