from django.shortcuts import render

# Create your views here.

def contenido(request):
    data={
        "img1" : "got.jpg",
        "img2" : "pb.jpg",
        "img3" : "ba.jpg"
    }
    return(request, "menuApp.html", data)