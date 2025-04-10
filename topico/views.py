from django.shortcuts import render, redirect
from django.http import HttpResponse
import banco
def index(response):
    return render(response, "topico/index.html")
def add(request):
    condição = 0
    if request.method == "POST":
        try:
            banco.adicionar(str(request.POST.get('nome')),str(request.POST.get('password')))
            return redirect('topico:index')
        except:
            condição = 1
    context={
        "erro":condição
    }
    
    return render(request, 'topico/add.html', context)














