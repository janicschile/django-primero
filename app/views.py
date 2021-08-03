from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import json


def index(request):
    return HttpResponse("<h1>ESTAS EN EL BLOG</h1> <ul><li>blog1</li><li>blog2</li><li>blog3</li></ul>")

def root(request):
    return redirect ("/blogs")

def nuevo(request):
    return HttpResponse("<h1>ESTAS EN EL BLOG</h1> <br> <p> Crear un nuevo blog </p>")

def crear(request):
    return redirect ("/")

def mostrar(request,number):
    return HttpResponse(f"<h1>ESTAS EN EL BLOG</h1> <br> <p> Mostrar Blog numero: {number}</p>")

def editar(request,number):
    return HttpResponse(f"<h1>ESTAS EN EL BLOG</h1> <br> <p> Editar el blog numero: {number}</p>")

def borrar(request,number):
    return redirect ("/")

def json1(request):
    data  =[
        {
            "nombre": "Oscar Guerrero G.", 
            "email": "oguerrerog@gmail.com"
        }, 
        {
            "name": "Elon Musk", 
            "email": "elon@tesla.com"
        }]
    
    data_str =json.dumps (data)
    return JsonResponse(data, safe=False)