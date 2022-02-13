from django.shortcuts import render
from django.http import HttpResponse
import re, math, html
from cipher.fn import *
from cipher.riddle_tables import show_table
from cipher.python_playground import myeval, myexec

def action(request, action_number):
    return eval('action_' + str(action_number) +'(request)' )

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
    key = re.sub(r"[^a-zA-Z0-9]", "", key_before_trunc)
    option_1 = request.POST.getlist("opt_1")[0]
    if option_1 == '1':
        nc = True
    else:
        nc = False

    output_text = ''
    output_text += '<B>Vigenere</B>'
    output_text += '<br>'
    output_text += 'Used key: ' + key
    output_text += '<br><br>'
    output_text += 'Decoded: ' + vig_d(input_text, key, nc)
    output_text += '<br><br>'
    output_text += 'Encoded: ' + vig_e(input_text, key, nc)
    output_text += '<br><br>'
    output_text += 'Beaufort: ' + beaufort(input_text, key, nc)
    output_text += '<br><br>'
    output_text += 'Auto key decoded: ' + vig_d_auto(input_text, key, nc)
    output_text += '<br><br>'
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

    text= re.sub(r"[^a-zA-Z]", "", input_text).upper()

    roter_key = re.sub(r"[^a-zA-Z]", "", opt_5).upper().ljust(3, 'A')
    ringsetting_key = re.sub(r"[^a-zA-Z]", "", opt_6).upper().ljust(3, 'A')
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
        txt_trunc = re.sub(r"[^0-9]", "", txt)

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
    output_text += '<br>'
    output_text += '<B>Wabun Morse Encode</B>'
    output_text += '<br>'
    output_text +=  morse_wabun_e(input_text)
    output_text += '<br>'
    output_text += '<B>Wabun Morse Decode</B>'
    output_text += '<br>'
    output_text +=  morse_wabun_d(input_text)

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
    input_text = re.sub(r"[^a-zA-Z0-9,]", "", input_text).upper()
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
            'US keyboard right shift',
            'US keyboard right <-> left',
            'US keyboard up <-> down',
            'US keyboard to Dvorak keyboard',
            'Dvorak keyboard to US keyboard',
            'US keyboard to MALTRON keyboard',
            'MALTRON keyboard to US keyboard']

    for menu in menus:
        output_text += menu + ': ' + table_subtitution(input_text, menu) + '<br>'

    return HttpResponse(output_text)

def action_17(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    option_1 = request.POST.getlist("opt_1")[0]

    output_text = ''

    tables ={
        '#International Radiotelephony Spelling Alphabet (NATO phonetic alphabet)':spelling_alphabet_icao_2008,
        '#1951 ICAO code words':spelling_alphabet_icao_1951,
        '#1949 ICAO code words':spelling_alphabet_icao_1949,
        '#1947 ICAO Latin America/Caribbean':spelling_alphabet_icao_1947_1,
        '#1947 ICAO alphabet':spelling_alphabet_icao_1947_2
    }

    input_text_lower = input_text.lower()

    if option_1 == '0':
        output_text += '<B>Phonetic Alphabet Encode</B>' + '<br>'

        output_text += '<br>'
        output_text += 'Input text = <br>'
        output_text += input_text_lower + '<br>'
        output_text += '<br>'

        for table_description,table in tables.items():
            output_text += table_description + '<br>'
            output_text += return_phonetic_alphabet_values(table) + '<br><br>'
            output_text += phonetic_alphabet_e(input_text_lower, table) +'<br>'
            output_text += '<hr>'

    if option_1 == '1':
        output_text += '<B>Phonetic Alphabet Decode</B>' + '<br>'

        output_text += '<br>'
        output_text += 'Input text = <br>'
        output_text += input_text_lower + '<br>'
        output_text += '<br>'
        
        for table_description,table in tables.items():
            output_text += table_description + '<br>'
            output_text += return_phonetic_alphabet_values(table) + '<br><br>'
            output_text += phonetic_alphabet_d(input_text_lower, table) +'<br>'
            output_text += '<hr>'

    return HttpResponse(output_text)

def action_18(request):
    option_1 = request.POST.getlist("opt_1")[0]

    output_text = show_table(int(option_1))
    
    return HttpResponse(output_text)

def action_19(request):
    input_text = request.POST.getlist("input_1_txt")[0]

    output_text = ''
    output_text += '<B>Text Analysis</B>' + '<br>'
    output_text += 'Text length = ' + str(len(input_text)) + '<br>'
    output_text += 'Used characters (unique) = ' + unique(input_text, sort=True) + '<br>'
    output_text += '' + '<br>'

    output_text += '<B>Letter frequency (Sorted Alphabetically)</B>' + '<br>'
    freq = letter_frequency(input_text,0,False)
    for i in freq:
        output_text += i[0] + ': ' + str(i[1]) + '<br>'
    output_text += '' + '<br>'

    output_text += '<B>Letter frequency (Sorted by Frequency)</B>' + '<br>'
    freq = letter_frequency(input_text,1,True)
    for i in freq:
        output_text += i[0] + ': ' + str(i[1]) + '<br>'
    output_text += '' + '<br>'

    return HttpResponse(output_text)

def action_20(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    ascii_list = adec(input_text)
    ascii_list_str = list(map(str, ascii_list))

    output_text = ''

    output_text += 'ASCII code (Binary)' + '<br>'
    output_text += ' '.join(base_a_to_base_b(ascii_list_str, 10, 2)) + '<br>'
    output_text += '' + '<br>'

    output_text += 'ASCII code (Octal)' + '<br>'
    output_text += ' '.join(base_a_to_base_b(ascii_list_str, 10, 8)) + '<br>'
    output_text += '' + '<br>'

    output_text += 'ASCII code (Decimal)' + '<br>'
    output_text += ' '.join(ascii_list_str) + '<br>'
    output_text += '' + '<br>'

    output_text += 'ASCII code (Hex)' + '<br>'
    output_text += ' '.join(base_a_to_base_b(ascii_list_str, 10, 16)) + '<br>'
    output_text += '' + '<br>'

    output_text += 'Base32' + '<br>'
    output_text += str(base64.b32encode(input_text.encode()))[2:-1] + '<br>'
    output_text += '' + '<br>'

    output_text += 'Base64' + '<br>'
    output_text += str(base64.b64encode(input_text.encode()))[2:-1] + '<br>'
    output_text += '' + '<br>'

    output_text += 'UUencode' + '<br>'
    output_text += html.escape(str(uu_encode(input_text.encode()))[2:-1]) + '<br>'
    output_text += '' + '<br>'

    output_text += 'ASCII85' + '<br>'
    output_text += html.escape(str(base64.a85encode(input_text.encode()))[2:-1]) + '<br>'
    output_text += '' + '<br>'

    output_text += 'BASE85' + '<br>'
    output_text += html.escape(str(base64.b85encode(input_text.encode()))[2:-1]) + '<br>'
    output_text += '' + '<br>'

    output_text += '' + '<br>'

    return HttpResponse(output_text)

def action_21(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    input_list = input_text.split()
    
    output_text = ''
    output_text += 'Input text was interpreted as: ' + ' '.join(input_list) + '<br>'    
    output_text += '' + '<br>'

    output_text += 'ASCII code (Binary)' + '<br>'
    temp_list = base_a_to_base_b(input_list,2,10)
    output_text += 'Decimal presentation: ' + ' '.join(temp_list) + '<br>'
    output_text += 'ASCII: ' + deca(temp_list) + '<br>'
    output_text += '' + '<br>'

    output_text += 'ASCII code (Octal)' + '<br>'
    temp_list = base_a_to_base_b(input_list,8,10)
    output_text += 'Decimal presentation: ' + ' '.join(temp_list) + '<br>'
    output_text += 'ASCII: ' + deca(temp_list) + '<br>'
    output_text += '' + '<br>'

    output_text += 'ASCII code (Decimal)' + '<br>'
    temp_list = base_a_to_base_b(input_list,10,10)
    output_text += 'Decimal presentation: ' + ' '.join(temp_list) + '<br>'
    output_text += 'ASCII: ' + deca(input_list) + '<br>'
    output_text += '' + '<br>'
    
    output_text += 'ASCII code (Hex)' + '<br>'
    temp_list = base_a_to_base_b(input_list,16,10)
    output_text += 'Decimal presentation: ' + ' '.join(temp_list) + '<br>'
    output_text += 'ASCII: ' + deca(temp_list) + '<br>'
    output_text += '' + '<br>'

    return HttpResponse(output_text)

def action_22(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    output_text = ''

    def output_template(byte):
        output_text = ''
        output_text += 'to base16: ' + str(base64.b16encode(byte))[2:-1] + '<br>'
        output_text += 'to base32: ' + str(base64.b32encode(byte))[2:-1] + '<br>' 
        output_text += 'to base64: ' + str(base64.b64encode(byte))[2:-1] + '<br>' 
        output_text += 'to uuencode: ' + html.escape(str(uu_encode(byte))[2:-1]) + '<br>' 
        output_text += 'to ascii85: ' + html.escape(str(base64.a85encode(byte))[2:-1]) + '<br>' 
        output_text += 'to base85: ' + html.escape(str(base64.b85encode(byte))[2:-1]) + '<br>' 
        output_text += 'to text: ' + html.escape(str(byte)[2:-1]) + '<br>'
        output_text += '<br>'
        return output_text
    

    input_text_formatted = input_text.upper()[:len(input_text)-(len(input_text) %2)]
    output_text += '<B>Base16 decode</B>'+'<br>'
    output_text += 'input: ' + input_text_formatted + '<br>'
    try:
        temp_byte = base64.b16decode(input_text_formatted)
        output_text += output_template(temp_byte)
    except:
        output_text += '# text was not interpreted as Base16 encoding. <br><br>' 
    
    input_text_formatted = input_text.upper()
    input_text_formatted = input_text_formatted + "="*(-len(input_text_formatted) %8)
    output_text += '<B>Base32 decode</B>'+'<br>'
    output_text += 'input: ' + input_text_formatted + '<br>'
    try:
        temp_byte = base64.b32decode(input_text_formatted)
        output_text += output_template(temp_byte)
    except:
        output_text += '# text was not interpreted as Base32 encoding. <br><br>' 

    input_text_formatted = input_text + "="*(-len(input_text) %4)
    output_text += '<B>Base64 decode</B>'+'<br>'
    output_text += 'input: ' + input_text_formatted + '<br>'
    try:
        temp_byte = base64.b64decode(input_text_formatted, validate=True)
        output_text += output_template(temp_byte)
    except:
        output_text += '# text was not interpreted as Base64 encoding. <br><br>' 

    input_text_formatted = input_text + " "*(-len(input_text) %4)
    output_text += '<B>UU decode</B>'+'<br>'
    output_text += 'input: ' + input_text_formatted + '<br>'
    try:
        temp_byte = uu_decode(input_text_formatted)
        output_text += output_template(temp_byte)
    except:
        output_text += '# text was not interpreted as UU encoding. <br><br>' 

    input_text_formatted = input_text
    output_text += '<B>ASCII85 decode</B>'+'<br>'
    output_text += 'input: ' + input_text_formatted + '<br>'
    try:
        temp_byte = base64.a85decode(input_text_formatted)
        output_text += output_template(temp_byte)
    except:
        output_text += '# text was not interpreted as ASCII85 encoding. <br><br>' 

    input_text_formatted = input_text
    output_text += '<B>Base85 decode</B>'+'<br>'
    output_text += 'input: ' + input_text_formatted + '<br>'
    try:
        temp_byte = base64.b85decode(input_text_formatted)
        output_text += output_template(temp_byte)
    except:
        output_text += '# text was not interpreted as Base85 encoding. <br><br>' 

    return HttpResponse(output_text)


def action_23(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    option_1 = request.POST.getlist("opt_1")[0]
    
    output_text = ''
    output_text += 'Text length = '+ str(len(input_text)) + '<br>'
    output_text += '' + '<br>'

    for i in range(2, math.ceil(len(input_text)/2)+1):
        if len(input_text) %i == 0 or option_1 == '1':
            output_text += '<B>Column count = '+ str(i) + '</B><br>'
            output_text += rect(input_text, i) + '<br>'

    output_text += '' + '<br>'

    return HttpResponse(output_text)

def action_24(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    key_before_trunc = request.POST.getlist("input_2_txt")[0]  
    key = re.sub(r"[^a-zA-Z0-9]", "", key_before_trunc)
    key = key.upper()
    key_assigned = assign_digits(key)
    
    output_text = ''
    output_text += 'Text length = '+ str(len(input_text)) + '<br>'
    output_text += 'Key strings = ' + key + '<br>'
    output_text += 'Key strings is interpretted as ' + str(key_assigned) + '<br>'
    output_text += '' + '<br>'
    output_text += 'Periodic Transposition Encode: ' + periodic_transposition_e(input_text, key_assigned) + '<br>'
    output_text += 'Periodic Transposition Decode: ' + periodic_transposition_d(input_text, key_assigned) + '<br>'

    output_text += '' + '<br>'

    return HttpResponse(output_text)

def action_25(request):
    input_text = request.POST.getlist("input_1_txt")[0]    
    output_text = ''
    output_text += '<br>'

    output_text += swap_xy_axes(input_text) + '<br>'

    output_text += '' + '<br>'

    return HttpResponse(output_text)

def action_26(request):
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

    input_text_working = input_text
    for i in text_del:
        input_text_working = input_text_working.replace(i, '')

    output_text = ''
    output_text += '<B>Characters replace</B>'
    output_text += '<br>'
    output_text +=  'Replace characters <br>'
    output_text += '_del: ' + text_del.upper() + "<br>"
    output_text += 'from: ' + text_from.upper() + "<br>"
    output_text += '__to: ' + text_to.upper() + '<br>'
    output_text += '<br>'
    output_text += '[Before]<br>'
    output_text += input_text + '<br>'
    output_text += '<br>'
    output_text += '[After]<br>'
    output_text += replace_all_case_insensitive(input_text_working, text_from, text_to)
    output_text += '<br>'
    output_text += '<br>'


    #frequency info
    output_text += '<B>Letter frequency</B>' + '<br>'
    analysys_text = re.sub(r"[^A-Z]", "", input_text.upper())

    total_letter_count = len(analysys_text)

    freq = letter_frequency(analysys_text,1,True)
    for i in range(len(freq)):
        output_text += freq[i][0] + ': ' + '{percent:.2%}'.format(percent=freq[i][1]/total_letter_count) +   ', '
        if i%9==8:
            output_text += '<br>'
    output_text += '' + '<br>'
    output_text += '' + '<br>'

    output_text += '<B>Bigram frequency</B>' + '<br>'
    analysys_text = re.sub(r"[^A-Z ]", "", input_text.upper())
    total_bigram_count = len(analysys_text) -1
    freq = bigram_frequency(analysys_text)
    for i in range(min(len(freq),18)):
        output_text += freq[i][0] + ': ' + '{percent:.2%}'.format(percent=freq[i][1]/total_bigram_count) +   ', '
        if i%9==8:
            output_text += '<br>'
    output_text += '' + '<br>'
    output_text += '' + '<br>'

    output_text += '<B>Basic English info.</B>' + '<br>'
    output_text += 'Letter frequency' + '<br>'
    output_text += 'E 12.49%, T 9.28%, A 8.04%, O 7.64%, I 7.57%, N 7.23%, S 6.51%, R 6.28%, H 5.05%' + '<br>'
    output_text += 'L 4.07%, D 3.82%, C 3.34%, U 2.73%, M 2.51%, F 2.40%, P 2.14%, G 1.87%, W 1.68%' + '<br>'
    output_text += 'Y 1.66%, B 1.48%, V 1.05%, K 0.54%, X 0.23%, J 0.16%, Q 0.12%, Z 0.09%' + '<br>'
    output_text += '' + '<br>'
    output_text += 'Bigram frequency' + '<br>'
    output_text += 'TH 3.56%, HE 3.07%, IN 2.43%, ER 2.05%, AN 1.99%, RE 1.85%, ON 1.76%, AT 1.49%, EN 1.45%' + '<br>'
    output_text += 'ND 1.35%, TI 1.34%, ES 1.34%, OR 1.28%, TE 1.20%, OF 1.17%, ED 1.17%, IS 1.13%, IT 1.12%' + '<br>'
    output_text += '' + '<br>'
    output_text += '* This is based on below site\'s great work. ' + '<br>'
    output_text += '<a href="https://norvig.com/mayzner.html">https://norvig.com/mayzner.html</a>' + '<br>'
    output_text += '' + '<br>'

    return HttpResponse(output_text)

def action_27(request):
    input_text = request.POST.getlist("input_1_txt")[0]    
    output_text = ''
    output_text += '<br>'
    output_text += html.escape(input_text).replace('\n','<BR>') +  '<br>'
    output_text += '<br>'

    if 'import ' in input_text:
        output_text += "Could not contain the strings 'import' by the security reason."
        return HttpResponse(output_text)
    elif 'eval(' in input_text:
        output_text += "Could not contain the strings 'eval' by the security reason."
        return HttpResponse(output_text)
    elif 'exec(' in input_text:
        output_text += "Could not contain the strings 'exec' by the security reason."
        return HttpResponse(output_text)

    try:
        result = myeval(input_text)
        if type(result) != "<type 'str'>":
            result = str(result)
        output_text += html.escape(result) + '<br>'
    except Exception as e:
        output_text += '# Python could not evaluate the expression. ' + '<br>'
        output_text += html.escape(str(e)) + '<br>'

    output_text += '<br>'
    output_text += '<br>'
    output_text += "Modules 'math', 'sympy', and 're' are available." + '<br>'

    return HttpResponse(output_text)

def action_28(request):
    input_text = request.POST.getlist("input_1_txt")[0]    
    output_text = ''
    output_text += '<br>'
    output_text += html.escape(input_text).replace('\n','<BR>') +  '<br>'
    output_text += '<br>'

    if 'import ' in input_text:
        output_text += "Could not contain the strings 'import' by the security reason."
        return HttpResponse(output_text)
    elif 'eval(' in input_text:
        output_text += "Could not contain the strings 'eval' by the security reason."
        return HttpResponse(output_text)
    elif 'exec(' in input_text:
        output_text += "Could not contain the strings 'exec' by the security reason."
        return HttpResponse(output_text)

    ldict = {'val':''}

    try:
        myexec(input_text,globals(),ldict)
        val = ldict['val']
        if type(val) != "<type 'str'>":
            val = str(val)
        if val =='':
            output_text += "# Please overwrite the variable 'val'." + '<br>'
        else:
            output_text += html.escape(val) + '<br>'
    except Exception as e:
        output_text += '# Python could not excute the expression. ' + '<br>'
        output_text += html.escape(str(e)) + '<br>'

    output_text += '<br>'
    output_text += '<br>'
    output_text += "Modules 'math', 'sympy', and 're' are available." + '<br>'

    return HttpResponse(output_text)

def action_29(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    input_text2 = request.POST.getlist("input_2_txt")[0]
    ngram = input_text2.upper()

    output_text = ''
    output_text += '<B>Vigenere break helper (key length)</B>'
    output_text += '<br>'
    output_text += 'Analysis Text<br>'
    analysys_text = re.sub(r"[^A-Z ]", "", input_text.upper())
    analysys_text_wo_space = re.sub(r"[^A-Z]", "", input_text.upper())
    output_text += analysys_text + '<br><br>'
    output_text += 'Text length: ' + str(len(analysys_text)) + ', wo space: '+ str(len(analysys_text_wo_space)) + '<br><br>'

    #frequency info
    output_text += '<B>Bigram appearance count</B>' + '<br>'
    total_bigram_count = len(analysys_text) -1
    freq = bigram_frequency(analysys_text)
    for i in range(min(len(freq),18)):
        output_text += freq[i][0] + ': ' + str(freq[i][1]) +   ', '
        if i%9==8:
            output_text += '<br>'
    output_text += '' + '<br>'

    output_text += '<B>Trigram appearance count</B>' + '<br>'
    total_trigram_count = len(analysys_text) -1
    freq = trigram_frequency(analysys_text)
    for i in range(min(len(freq),18)):
        output_text += freq[i][0] + ': ' + str(freq[i][1]) +   ', '
        if i%9==8:
            output_text += '<br>'
    output_text += '' + '<br>'
    output_text += '' + '<br>'

    output_text += '<B>n-gram distance</B>' + '<br>'
    output_text += 'distance: count' + '<br>'
    freq = ngram_distance(analysys_text, ngram)
    for i in range(min(len(freq),20)):
        output_text += str(freq[i][0]) + ': ' + str(freq[i][1]) +   '<br>'

    output_text += '' + '<br>'
    output_text += '' + '<br>'
    output_text += '' + '<br>'
    output_text += '' + '<br>'

    return HttpResponse(output_text)

def action_30(request):
    input_text = request.POST.getlist("input_1_txt")[0]

    output_text = ''
    output_text += '<B>Hash</B>' + '<br>'
    output_text += '' + '<br>'
    
    output_text += 'Text___: ' + input_text + '<br>'
    output_text += '' + '<br>'

    output_text += 'MD5____: ' + hashlib.md5(input_text.encode()).hexdigest() + '<br>'
    output_text += 'SHA1___: ' + hashlib.sha1(input_text.encode()).hexdigest() + '<br>'
    output_text += 'SHA224_: ' + hashlib.sha224(input_text.encode()).hexdigest() + '<br>'
    output_text += 'SHA256_: ' + hashlib.sha256(input_text.encode()).hexdigest() + '<br>'
    output_text += 'SHA384_: ' + hashlib.sha384(input_text.encode()).hexdigest() + '<br>'
    output_text += 'SHA512_: ' + hashlib.sha512(input_text.encode()).hexdigest() + '<br>'
    output_text += 'BLAKE2b: ' + hashlib.blake2b(input_text.encode()).hexdigest() + '<br>'
    output_text += 'BLAKE2s: ' + hashlib.blake2s(input_text.encode()).hexdigest() + '<br>'
    output_text += '' + '<br>'


    return HttpResponse(output_text)

def action_31(request):
    input_text = request.POST.getlist("input_1_txt")[0]
    option_1 = request.POST.getlist("opt_1")[0]

    output_text = ''
    output_text += 'Chemical Symbol <BR>'
    output_text += chemical_symbol_convert(input_text, option_1)

    return HttpResponse(output_text)
