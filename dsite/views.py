from django.http import HttpResponse
from django.shortcuts import render

def index(respons):
    context={
        "nome":"vic"
    }
    return render(respons, 'dsite/index.html', context)



