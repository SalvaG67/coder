from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def saludar(request):
    return HttpResponse("hola desde django")
def saludar_con_etiqueta(request):
    return HttpResponse("<h1>hola desde django</h1>")