from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

tool_template = 'tool_template.html'

input_1 = '<textarea id="input_1_txt" class="inputtextarea1"></textarea><BR>'
input_1_num = '<textarea id="input_1_txt" class="inputtextarea1" inputmode="numeric"></textarea><BR>'
input_2_key = '<p>Key<p><textarea id="input_2_txt" class="inputtextarea2"></textarea><BR>'
clear_1 = 'document.getElementById( "input_1_txt" ).value =""'
clear_2 = 'document.getElementById( "input_2_txt" ).value =""'
data_field_1 = '"input_1_txt": document.getElementById( "input_1_txt" ).value,'
data_field_2 = '"input_2_txt": document.getElementById( "input_2_txt" ).value,'
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
        'action_url':'"./action_a"',
    })

def page2(request):
    return render(request, tool_template, 
    {
        'title':'Railfence',
        'fields':[input_1],
        'clears':[clear_1],
        'data_fields':[data_field_1],
        'options':'',
        'action_url':'"./action_c"',
    })

def page3(request):
    return render(request, tool_template, 
    {
        'title':'Prime factorize',
        'fields':[input_1_num],
        'clears':[clear_1],
        'data_fields':[data_field_1],
        'options':'',
        'action_url':'"./action_e"',
    })

def page4(request):
    return render(request, tool_template, 
    {
        'title':'Vigenere',
        'fields':[input_1,input_2_key],
        'clears':[clear_1,clear_2],
        'data_fields':[data_field_1, data_field_2,data_opt_1],
        'options':[option_numeric_flag],
        'action_url':'"./action_b"',
    })

def page5(request):
    return render(request, tool_template, 
    {
        'title':'Columnar',
        'fields':[input_1,input_2_key],
        'clears':[clear_1,clear_2],
        'data_fields':[data_field_1, data_field_2],
        'options':'',
        'action_url':'"./action_d"',
    })

def page6(request):
    return render(request, tool_template, 
    {
        'title':'Playfair',
        'fields':[input_1],
        'clears':[clear_1],
        'data_fields':[data_field_1],
        'options':'',
        'action_url':'"./action_f"',
    })

