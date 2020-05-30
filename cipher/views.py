from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

tool_template = 'tool_template.html'

input_1 = '<textarea id="input_1_txt" class="inputtextarea1"></textarea><BR>'
input_1_num = '<textarea id="input_1_txt" class="inputtextarea1" inputmode="numeric"></textarea><BR>'
input_2 = '<textarea id="input_2_txt" class="inputtextarea2"></textarea><BR>'
input_3 = '<textarea id="input_3_txt" class="inputtextarea2"></textarea><BR>'
input_2_key = '<p>Key<p><textarea id="input_2_txt" class="inputtextarea2"></textarea><BR>'
input_1_num_m = '<div style="float:left;"><p>m:</p></div><div style="float:left;" width="100%"><textarea id="input_1_txt" class="inputtextarea2" inputmode="numeric""></textarea></div><div style="clear:both;"></div>'
input_2_num_e = '<div style="float:left;"><p>e:</p></div><div style="float:left;" width="100%"><textarea id="input_2_txt" class="inputtextarea2" inputmode="numeric""></textarea></div><div style="clear:both;"></div>'
input_3_num_n = '<div style="float:left;"><p>n:</p></div><div style="float:left;" width="100%"><textarea id="input_3_txt" class="inputtextarea2" inputmode="numeric""></textarea></div><div style="clear:both;"></div>'
input_4_num_p = '<div style="float:left;"><p>p:</p></div><div style="float:left;" width="100%"><textarea id="input_4_txt" class="inputtextarea2" inputmode="numeric""></textarea></div><div style="clear:both;"></div>'
input_5_num_q = '<div style="float:left;"><p>q:</p></div><div style="float:left;" width="100%"><textarea id="input_5_txt" class="inputtextarea2" inputmode="numeric""></textarea></div><div style="clear:both;"></div>'
input_1_num_length = '<p>Length<p><textarea id="input_1_txt" class="inputtextarea2" inputmode="numeric"></textarea><BR>'
input_2_from = '<p>from<p><textarea id="input_2_txt" class="inputtextarea2"></textarea><BR>'
input_3_to = '<p>to<p><textarea id="input_3_txt" class="inputtextarea2"></textarea><BR>'
input_2_num = '<textarea id="input_2_txt" class="inputtextarea2" inputmode="numeric"></textarea><BR>'
clear_1 = 'document.getElementById( "input_1_txt" ).value =""'
clear_2 = 'document.getElementById( "input_2_txt" ).value =""'
clear_3 = 'document.getElementById( "input_3_txt" ).value =""'
clear_4 = 'document.getElementById( "input_4_txt" ).value =""'
clear_5 = 'document.getElementById( "input_5_txt" ).value =""'
data_field_1 = '"input_1_txt": document.getElementById( "input_1_txt" ).value,'
data_field_2 = '"input_2_txt": document.getElementById( "input_2_txt" ).value,'
data_field_3 = '"input_3_txt": document.getElementById( "input_3_txt" ).value,'
data_field_4 = '"input_4_txt": document.getElementById( "input_4_txt" ).value,'
data_field_5 = '"input_5_txt": document.getElementById( "input_5_txt" ).value,'
data_opt_1 = '"opt_1": document.getElementById( "opt_1" ).value,'

option_numeric_flag = \
'''
        <div class="cp_ipselect cp_sl01">
            <select required id=opt_1>
                <option value="" hidden>Choose</option>
                <option value="0" selected>Non-effective for numerics</option>
                <option value="1">Effective for numerics</option>
            </select>
        </div>
'''

option_en_dec_mode = \
'''
        <div class="cp_ipselect cp_sl01">
            <select required id=opt_1>
                <option value="" hidden>Choose</option>
                <option value="0" selected>Encode</option>
                <option value="1">Decode</option>
            </select>
        </div>
'''

option_password_generator = \
'''
        <div class="cp_ipselect cp_sl01">
            <select required id=opt_1>
                <option value="" hidden>Choose</option>
                <option value="0" selected>A-Z, a-z, 0-9</option>
                <option value="1">A-Z, a-z, 0-9, !@#$%^&</option>
                <option value="2">A-Z, a-z</option>
                <option value="3">A-Z</option>
                <option value="4">a-z</option>
                <option value="5">0-9</option>
                <option value="6">A-Z, a-z, !@#$%^&</option>
                <option value="7">A-Z, 0-9</option>
                <option value="8">a-z, 0-9</option>
            </select>
        </div>
'''

option_separater = \
'''
        <div class="cp_ipselect cp_sl01">
            <select required id=opt_1>
                <option value="" hidden>Choose</option>
                <option value="0" selected> (space)</option>
                <option value="1">,</option>
                <option value="2"> (new line)</option>
            </select>
        </div>
'''

def index(request):
    return render(request, 'index.html', {})



def page1(request):
    return render(request, tool_template, 
    {
        'title':'ROT and Atbash',
        'fields':[input_1],
        'clears':[clear_1],
        'data_fields':[data_field_1,data_opt_1],
        'options':[option_numeric_flag],
        'action_url':'"./action_1"',
    })

def page2(request):
    return render(request, tool_template, 
    {
        'title':'Railfence and Reverse',
        'fields':[input_1, "<p>Offset<p>" + input_2_num],
        'clears':[clear_1, clear_2],
        'data_fields':[data_field_1, data_field_2],
        'options':'',
        'action_url':'"./action_2"',
    })

def page3(request):
    return render(request, tool_template, 
    {
        'title':'Prime factor',
        'fields':[input_1_num],
        'clears':[clear_1],
        'data_fields':[data_field_1],
        'options':'',
        'action_url':'"./action_3"',
    })

def page4(request):
    return render(request, tool_template, 
    {
        'title':'Vigenere',
        'fields':[input_1,input_2_key],
        'clears':[clear_1,clear_2],
        'data_fields':[data_field_1, data_field_2,data_opt_1],
        'options':[option_numeric_flag],
        'action_url':'"./action_4"',
    })

def page5(request):
    return render(request, tool_template, 
    {
        'title':'Columnar',
        'fields':[input_1,input_2_key],
        'clears':[clear_1,clear_2],
        'data_fields':[data_field_1, data_field_2],
        'options':'',
        'action_url':'"./action_5"',
    })

def page6(request):
    return render(request, tool_template, 
    {
        'title':'Playfair',
        'fields':[input_1],
        'clears':[clear_1],
        'data_fields':[data_field_1],
        'options':'',
        'action_url':'"./action_6"',
    })

def page7(request):
    return render(request, 'tool_template_enigma.html', 
    {
        'title':'Enigma',
        'fields':[input_1],
        'clears':[clear_1],
        'data_fields':[data_field_1],
        'options':'',
        'action_url':'"./action_7"',
    })

def page8(request):
    return render(request, tool_template, 
    {
        'title':'RSA',
        'fields':[input_1_num_m, input_2_num_e, input_3_num_n, input_4_num_p, input_5_num_q],
        'clears':[clear_1, clear_2, clear_3, clear_4, clear_5],
        'data_fields':[data_field_1, data_field_2, data_field_3, data_field_4, data_field_5],
        'options':'',
        'action_url':'"./action_8"',
    })

def page9(request):
    return render(request, tool_template, 
    {
        'title':'Password generator',
        'fields':[input_1_num_length],
        'clears':[clear_1],
        'data_fields':[data_field_1, data_opt_1],
        'options':[option_password_generator],
        'action_url':'"./action_9"',
    })

def page10(request):
    return render(request, tool_template, 
    {
        'title':'Morse',
        'fields':[input_1],
        'clears':[clear_1],
        'data_fields':[data_field_1],
        'options':'',
        'action_url':'"./action_10"',
    })

def page11(request):
    return render(request, tool_template, 
    {
        'title':'Characters replace',
        'fields':[input_1, input_2_from, input_3_to],
        'clears':[clear_1, clear_2, clear_3],
        'data_fields':[data_field_1, data_field_2, data_field_3],
        'options':'',
        'action_url':'"./action_11"',
    })

def page12(request):
    return render(request, tool_template, 
    {
        'title':'Affine cipher',
        'fields':[input_1],
        'clears':[clear_1],
        'data_fields':[data_field_1, data_opt_1],
        'options':[option_en_dec_mode],
        'action_url':'"./action_12"',
    })

def page13(request):
    return render(request, tool_template, 
    {
        'title':'Text split',
        'fields':[input_1, "<p>length<p>" + input_2_num],
        'clears':[clear_1, clear_2],
        'data_fields':[data_field_1, data_field_2, data_opt_1],
        'options':[option_separater],
        'action_url':'"./action_13"',
    })

def page14(request):
    return render(request, tool_template, 
    {
        'title':'Number converter',
        'fields':[input_1, "<p>from base<p>" + input_2_num],
        'clears':[clear_1, clear_2],
        'data_fields':[data_field_1, data_field_2],
        'options':'',
        'action_url':'"./action_14"',
    })

def page15(request):
    return render(request, tool_template, 
    {
        'title':'Words index',
        'fields':[input_1, "<p># of words<p>" + input_2, "<p># of letters<p>" + input_3],
        'clears':[clear_1, clear_2, clear_3],
        'data_fields':[data_field_1, data_field_2, data_field_3],
        'options':'',
        'action_url':'"./action_15"',
    })

def page16(request):
    return render(request, tool_template, 
    {
        'title':'Simple substitution',
        'fields':[input_1],
        'clears':[clear_1],
        'data_fields':[data_field_1],
        'options':'',
        'action_url':'"./action_16"',
    })