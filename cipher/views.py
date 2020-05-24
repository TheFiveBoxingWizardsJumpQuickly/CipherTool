from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    param = 'Cipher tool (under construction)'
    return render(request, 'index.html', {
        'header_string': param,
        })
