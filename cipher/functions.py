from django.shortcuts import render
from django.http import HttpResponse
from cipher.fn import rot, atbash, vig_e, vig_d, beaufort, vig_d_auto, vig_e_auto

def decode_a(request):
    input_text = request.POST.getlist("input_1_txt")[0]

    output_text = ''
    output_text += '<B>Atbash</B>'
    output_text += '<br>'
    output_text +=  atbash(input_text)

    output_text += '<br>'

    output_text += '<br>'
    output_text += '<B>ROT</B>'
    output_text += '<br>'
    for i in range(26):
        output_text += str(i).zfill(2) + ': '
        output_text += rot(input_text,i)
        output_text += '<br>'
    
    output_text += '<br>'
    output_text += '<B>ROT and Atbash</B>'
    output_text += '<br>'
    for i in range(26):
        output_text += str(i).zfill(2) + ': '
        output_text += atbash(rot(input_text,i))
        output_text += '<br>'


    return HttpResponse(output_text)

def decode_b(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    key = request.POST.getlist("input_2_txt")[0]  

    output_text = ''
    output_text += '<B>Vigenere</B>'
    output_text += '<br>'
    output_text += 'Decode: ' + vig_d(input_text, key)
    output_text += '<br>'
    output_text += 'Encode: ' + vig_e(input_text, key)
    output_text += '<br>'
    output_text += 'Beaufort: ' + beaufort(input_text, key)
    output_text += '<br>'
    output_text += 'Auto key decode: ' + vig_d_auto(input_text, key)
    output_text += '<br>'
    output_text += 'Auto key encode: ' + vig_e_auto(input_text, key)
    return HttpResponse(output_text)