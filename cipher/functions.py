from django.shortcuts import render
from django.http import HttpResponse
import re
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
    offset_text = request.POST.getlist("input_2_txt")[0]  
    if offset_text == '':
        offset = 0
    else:
        offset = int(offset_text)

    output_text = ''
    output_text += '<B>Reverse</B>'
    output_text += '<br>'
    output_text += rev(input_text) + '<br>'
    output_text += '<br>'

    output_text += '<B>Railfence</B>'
    output_text += '<br>'
    output_text += 'Offset = ' + str(offset) + '<br>'
    for i in range(2, len(input_text)):
        output_text += str(i).zfill(3) + ': '
        output_text += railfence_d(input_text,i, offset)
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
    key_before_trunc = request.POST.getlist("input_2_txt")[0]  
    key = re.sub(r"[^a-zA-Z0-9_]", "", key_before_trunc)
    option_1 = request.POST.getlist("opt_1")[0]
    if option_1 == '1':
        nc = True
    else:
        nc = False

    output_text = ''
    output_text += '<B>Vigenere</B>'
    output_text += '<br>'
    output_text += 'Used key: ' + key
    output_text += '<br>'
    output_text += 'Decoded: ' + vig_d(input_text, key, nc)
    output_text += '<br>'
    output_text += 'Encoded: ' + vig_e(input_text, key, nc)
    output_text += '<br>'
    output_text += 'Beaufort: ' + beaufort(input_text, key, nc)
    output_text += '<br>'
    output_text += 'Auto key decoded: ' + vig_d_auto(input_text, key, nc)
    output_text += '<br>'
    output_text += 'Auto key encoded: ' + vig_e_auto(input_text, key, nc)
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

def action_10(request):
    input_text = request.POST.getlist("input_1_txt")[0]

    output_text = ''
    output_text += '<B>Morse Encode</B>'
    output_text += '<br>'
    output_text +=  morse_e(input_text)
    output_text += '<br>'
    output_text += '<B>Morse Decode</B>'
    output_text += '<br>'
    output_text +=  morse_d(input_text)

    return HttpResponse(output_text)

def action_11(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    input_from = request.POST.getlist("input_2_txt")[0]
    input_to = request.POST.getlist("input_3_txt")[0]

    text_from = unique(input_from)
    text_to = input_to
    
    text_length = min(len(text_from), len(text_to))
    text_del = text_from[text_length:]
    text_from = text_from[:text_length]
    text_to = text_to[:text_length]
    map_dict = dict(zip(text_from, text_to))

    for i in text_del:
        input_text = input_text.replace(i, '')

    output_text = ''
    output_text += '<B>Characters replace</B>'
    output_text += '<br>'
    output_text +=  'Replace characters <br>'
    output_text += '_del: ' + text_del + "<br>"
    output_text += 'from: ' + text_from + "<br>"
    output_text += '__to: ' + text_to + '<br>'
    output_text += '<br>'
    output_text += replace_all(input_text, text_from, text_to)

    return HttpResponse(output_text)

def action_12(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    option_1 = request.POST.getlist("opt_1")[0]

    output_text = ''
    if option_1 == '0':
        output_text += '<B>Affine cipher encoding</B>'
        output_text += '<br>'
        for i in  [1,3,5,7,9,11,15,17,19,21,23,25]:
            for j in range(26):
                output_text += 'a=' + str(i).zfill(2) + ', b=' + str(j).zfill(2) + ': '
                output_text += affine_e(input_text,i,j)
                output_text += '<br>'
    elif option_1 == '1':      
        output_text += '<B>Affine cipher decoding</B>'
        output_text += '<br>'
        for i in [1,3,5,7,9,11,15,17,19,21,23,25]:
            for j in range(26):
                output_text += 'a=' + str(i).zfill(2) + ', b=' + str(j).zfill(2) + ': '
                output_text += affine_d(input_text,i,j)
                output_text += '<br>'
    return HttpResponse(output_text)

def action_13(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    length_text = request.POST.getlist("input_2_txt")[0]
    option_1 = request.POST.getlist("opt_1")[0]

    if length_text == '':
        length = 0
    else:
        length = int(length_text)

    map ={
        '0': ' ',
        '1': ',',
        '2': '<br>'
        }
    separater = map.get(option_1)

    output_text = ''
    output_text += '<B>Text split</B>'
    output_text += '<br>'
    output_text += 'split length: ' + str(length) + "<br>"
    output_text += '<br>'
    output_text += text_split(input_text, length, separater)

    return HttpResponse(output_text)

def action_14(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    base_text = request.POST.getlist("input_2_txt")[0]

    if base_text == '':
        base = 10
    else:
        base = int(base_text)

    input_text = input_text.replace(' ',',')
    input_text = re.sub(r"[^a-zA-Z0-9,_]", "", input_text).upper()
    nlist = input_text.split(',')
    output_text = ''
    output_text += '<B>Number conversion</B>'
    output_text += '<br>'
    output_text += 'Converting ' + ','.join(nlist) +  '<br>'
    output_text += 'from base: ' + str(base) + "<br>"
    
    output_text += 'to ascii: '
    output_text += ''.join(deca(base_a_to_base_b(nlist, base, 10)))
    output_text += '<br>'

    for i in range(2, 37):
        output_text += 'to base ' + str(i).zfill(2) + ': '
        output_text += ','.join(base_a_to_base_b(nlist, base, i))
        output_text += '<br>'

    return HttpResponse(output_text)

def action_15(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    word_index_text = request.POST.getlist("input_2_txt")[0]
    letter = request.POST.getlist("input_3_txt")[0]

    word_list = input_text.replace(' ',',').split(',')

    word_index_list_text = word_index_text.replace(' ',',').split(',')
    word_index_list=[]
    for i in word_index_list_text:
        word_index_list.append(int(i))
    
    letter_index_list_text = letter.replace(' ',',').split(',')
    letter_index_list=[]
    for i in letter_index_list_text:
        letter_index_list.append(int(i))

    count = min(len(word_index_list), len(letter_index_list))

    output_text = ''
    output_text += '<B>Word index</B>'
    output_text += '<br>'

    indexed_letters =''
    for i in range(count):
        output_text += 'word # ' + str(word_index_list[i]) + ' (' + word_list[word_index_list[i]-1] + ' ),'
        output_text += 'letter # ' + str(letter_index_list[i]) + ': '
        tmp = word_list[word_index_list[i]-1][letter_index_list[i]-1]
        output_text += tmp + '<br>'
        indexed_letters += tmp

    output_text += '<br>' + 'result: ' + indexed_letters

    return HttpResponse(output_text)

def action_16(request):
    input_text = request.POST.getlist("input_1_txt")[0]

    output_text = ''
    output_text += '<B>Simple substitutioin</B>'
    output_text += '<br>'

    menus =['A-a swap', 
            'Morse .- swap', 
            'Morse reverse', 
            'Morse .- swap and reverse', 
            'US keyboard left shift',
            'US keyboard right shift']

    for menu in menus:
        output_text += menu + ': ' + table_subtitution(input_text, menu) + '<br>'

    return HttpResponse(output_text)

