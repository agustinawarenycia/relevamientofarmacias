from django.http import HttpResponse
from django.template import context
from django.template.loader import get_template #cargador para simplificar ruteo
from django.shortcuts import render #ruteo mas simplificado


def hola(request):
    return HttpResponse("hola mundo")



def vista_principal(request):#vista principal
    #doc_externo = get_template('principal.html')
    
    #documento = doc_externo.render()

    return render(request,'principal.html') 

def vista_jufec(request): #vista pagina de jufec
    return render(request,"jufec.html")


def vista_prueba(request): #vista de prueba del login
    return render(request,"index.html")
   