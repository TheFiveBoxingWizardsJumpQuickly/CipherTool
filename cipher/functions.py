from django.shortcuts import render
from django.http import HttpResponse
from cipher.fn import *

def action_a(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    option_1 = request.POST.getlist("opt_1")[0]
    if option_1 == '1':
        nc = True
    else:
        nc = False

    output_text = ''
    output_text += '<B>Atbash</B>'
    output_text += '<br>'
    output_text +=  atbash(input_text,nc)

    output_text += '<br>'

    output_text += '<br>'
    output_text += '<B>ROT</B>'
    output_text += '<br>'
    for i in range(26):
        output_text += str(i).zfill(2) + ': '
        output_text += rot(input_text,i,nc)
        output_text += '<br>'
    
    output_text += '<br>'
    output_text += '<B>ROT and Atbash</B>'
    output_text += '<br>'
    for i in range(26):
        output_text += str(i).zfill(2) + ': '
        output_text += atbash(rot(input_text,i,nc))
        output_text += '<br>'


    return HttpResponse(output_text)

def action_b(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    key = request.POST.getlist("input_2_txt")[0]  
    option_1 = request.POST.getlist("opt_1")[0]
    if option_1 == '1':
        nc = True
    else:
        nc = False

    output_text = ''
    output_text += '<B>Vigenere</B>'
    output_text += '<br>'
    output_text += 'Decode: ' + vig_d(input_text, key, nc)
    output_text += '<br>'
    output_text += 'Encode: ' + vig_e(input_text, key, nc)
    output_text += '<br>'
    output_text += 'Beaufort: ' + beaufort(input_text, key, nc)
    output_text += '<br>'
    output_text += 'Auto key decode: ' + vig_d_auto(input_text, key, nc)
    output_text += '<br>'
    output_text += 'Auto key encode: ' + vig_e_auto(input_text, key, nc)
    return HttpResponse(output_text)

def action_c(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    output_text = ''
    output_text += '<B>Reverse</B>'
    output_text += '<br>'
    output_text += rev(input_text) + '<br>'
    output_text += '<br>'

    output_text += '<B>Railfence</B>'
    output_text += '<br>'
    for i in range(2, len(input_text)):
        output_text += str(i).zfill(3) + ': '
        output_text += railfence_d(input_text,i)
        output_text += '<br>'

    return HttpResponse(output_text)

def action_d(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    key = request.POST.getlist("input_2_txt")[0]
    output_text = ''

    output_text += '<B>Columnar decode</B>' + ' with key: ' + key
    output_text += '<br>'
    output_text += ''.join(columnar_d(input_text, assign_digits(key)))
    output_text += '<br>'
    output_text += '<br>'

    output_text += '<B>Columnar encode</B>' + ' with key: ' + key
    output_text += '<br>'
    output_text += ''.join(columnar_e(input_text, assign_digits(key)))

    return HttpResponse(output_text)

def action_e(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    extracted_input_text = extract_integer_only(input_text)

    if extracted_input_text == '':
        return HttpResponse('')
    else:            
        output_text = ''

        output_text += '<B>Prime factorize</B>'
        output_text += '<br>'
        output_text += factorize(extract_integer_only(input_text))
        
        return HttpResponse(output_text)

def action_f(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    output_text = ''

    output_text += '<B>Playfair decode</B>'
    output_text += '<br>'
    output_text += playfair_d(input_text)
    output_text += '<br>'
    output_text += '<br>'

    output_text += '<B>Playfair encode</B>'
    output_text += '<br>'
    output_text += playfair_e(input_text)

    return HttpResponse(output_text)
