from django.shortcuts import render
from django.http import HttpResponse
from cipher.fn import rot

def sample(request):
    input_text = request.POST.getlist("formName")
    output_text = rot(input_text[0],13)
    return HttpResponse(output_text)
