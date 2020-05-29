from django.shortcuts import render
from django.http import HttpResponse
from cipher.fn import *

def action_1(request):
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

def action_2(request):
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

def action_3(request):
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

def action_4(request):
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

def action_5(request):
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

def action_6(request):
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

def action_7(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    opt_1 = request.POST.getlist("opt_1")[0]
    opt_2 = request.POST.getlist("opt_2")[0]
    opt_3 = request.POST.getlist("opt_3")[0]
    opt_4 = request.POST.getlist("opt_4")[0]
    opt_5 = request.POST.getlist("opt_5")[0]
    opt_6 = request.POST.getlist("opt_6")[0]
    opt_7 = request.POST.getlist("opt_7")[0]

    import re
    text= re.sub(r"[^a-zA-Z_]", "", input_text).upper()

    roter_key = re.sub(r"[^a-zA-Z_]", "", opt_5).upper().ljust(3, 'A')
    ringsetting_key = re.sub(r"[^a-zA-Z_]", "", opt_6).upper().ljust(3, 'A')
    plugboard= plugboard_gen(opt_7)

    output_text = ''
    output_text += '<B>Enigma</B>'
    output_text += '<br>'
    output_text += 'Input text: ' + text + "<br>"
    output_text += 'Rotor set: ' + opt_1 + ' ' + opt_2 +' ' + opt_3 + "<br>"
    output_text += 'Reflector: ' + opt_4 + "<br>"
    output_text += 'Roter key: ' + roter_key  + "<br>"
    output_text += 'Ringsetting key: ' + ringsetting_key + "<br>"
    output_text += 'Plugboard: ' + ','.join(plugboard) + "<br>"
    output_text += '<br>'
    output_text += 'Enigma output: '

    #enigma(text, rotor_left_id, rotor_mid_id, rotor_right_id, reflector_id, rotor_key,ringsetting_key,plugboard):
    output_text += enigma(text, int(opt_1), int(opt_2), int(opt_3), opt_4,roter_key, ringsetting_key, plugboard)

    return HttpResponse(output_text)

def action_8(request):
    
    def force_int(txt):
        import re
        txt_trunc = re.sub(r"[^0-9_]", "", txt)

        if txt_trunc == '':
            return 0
        else:
            return int(txt_trunc)

    m = force_int(request.POST.getlist("input_1_txt")[0])
    e = force_int(request.POST.getlist("input_2_txt")[0])
    n = force_int(request.POST.getlist("input_3_txt")[0])
    p = force_int(request.POST.getlist("input_4_txt")[0])
    q = force_int(request.POST.getlist("input_5_txt")[0])

    output_text = ''
    output_text += '<B>RSA</B>'
    output_text += '<br>'
    output_text += 'm = ' + str(m) + '<br>'
    output_text += 'e = ' + str(e) + '<br>'
    output_text += 'n = ' + str(n) + '<br>'
    if m == 0 or e == 0 or n == 0: return HttpResponse(output_text)

    output_text += 'RSA Encode: ' + str(rsa_encode(m, e, n)) + '<br>'
    if p == 0 or q == 0: return HttpResponse(output_text)

    output_text += '<br>'
    output_text += 'p = ' + str(p) + '<br>'
    output_text += 'q = ' + str(q) + '<br>'
    output_text += 'check: p*q = ' + str(p*q) + '<br>'
    output_text += 'check: (n) = ' + str(n) + '<br>'

    [decode, d] = rsa_decode(m, e, n, p, q)
    if d == 0:
        output_text += 'Modular inverse does not exist <br>'
    else:
        output_text += 'calculated d = ' + str(rsa_decode(m, e, n, p, q)[1]) + '<br>'
        output_text += 'RSA Decode: ' + str(rsa_decode(m, e, n, p, q)[0]) + '<br>'

    return HttpResponse(output_text)

def action_9(request):
    text_length = request.POST.getlist("input_1_txt")[0]
    opt_1 = request.POST.getlist("opt_1")[0]

    list_symbol = '!@#$%^&'

    map ={
        '0': list_A + list_a + list_0,
        '1': list_A + list_a + list_0 + list_symbol,
        '2': list_A + list_a,
        '3': list_A,
        '4': list_a,
        '5': list_0,
        '6': list_A + list_a + list_symbol,
        '7': list_A + list_0,
        '8': list_a + list_0
    }
    table = map.get(opt_1)

    output_text = ''
    output_text += '<B>Password generator</B>'
    output_text += '<br>'
    output_text += 'Available Charactors: ' + table + "<br>"
    output_text += 'Length: ' + text_length + "<br>"
    output_text += '<br>'
    output_text += password_generate(int(text_length), table) 

    return HttpResponse(output_text)