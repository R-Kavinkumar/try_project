
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def func(response):
    kk="hi bey"
    ss={'disp':kk}
    return(render(response,"index.html",context=ss))