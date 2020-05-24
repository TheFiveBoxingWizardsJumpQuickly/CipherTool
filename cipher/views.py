from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    param = 'Hello, this is a cipher tool'
    return render(request, 'index.html', {
        'testparam': param,
        })
