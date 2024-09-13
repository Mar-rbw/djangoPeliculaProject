from django.shortcuts import render

# Create your views here.

def detallesGot(request):
    data = {
        "titulo": "Game of thorns",
        "descripcion": "Mala temporada 8",
        "valor" : "8"
    }
    return(request, "detalleApp.html", data)

def detallesPb(request):
    data = {
        "titulo": "prison Break",
        "descripcion": "No se",
        "valor" : "5"
    }
    return(request, "detalleApp.html", data)

def detallesBa(request):
    data = {
        "titulo": "Breking Bad",
        "descripcion": "JESSSI!!",
        "valor" : "1000/10"
    }
    return(request, "detalleApp.html", data)