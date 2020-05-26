from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return render(request, 'index.html', {})

def page1(request):
    return render(request, 'page1.html', {'title':'ROT and Atbash'})

def page2(request):
    return render(request, 'page2.html', {'title':'Railfence'})

def page3(request):
    return render(request, 'page3.html', {'title':'Prime factorize'})

def page4(request):
    return render(request, 'page4.html', {'title':'Vigenere'})

def page5(request):
    return render(request, 'page5.html', {'title':'Columnar'})

def page6(request):
    return render(request, 'page6.html', {'title':'Playfair'})