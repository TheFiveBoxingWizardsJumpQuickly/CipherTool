from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    param = 'Cipher tool (under construction)'
    return render(request, 'index.html', {
        'header_string': param,
        })

def page1(request):
    return render(request, 'page1.html', {'title':'ROT and Vigenere'})

def page2(request):
    return render(request, 'page2.html', {'title':'Transposition'})

def page3(request):
    return render(request, 'page3.html', {'title':'Math'})