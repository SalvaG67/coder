from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'saludo': 'primera "pagina" de mi web con django',
    }
    return render(request, 'myapp/index.html', context)
