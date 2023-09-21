from django.shortcuts import render

def Funcion(request):
    datos = {
        "Nombre" : "Lautaro"
    }
    return render(request,"Pag.html",datos)
# Create your views here.
