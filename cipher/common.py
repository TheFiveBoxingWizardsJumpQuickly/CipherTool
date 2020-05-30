def assign_digits(x):
    a=[0]*len(x)

    for i in range(len(x)):
        a[i]=[x[i],i]
        
    a.sort(key=lambda t:(t[0],t[1]))

    b=[0]*len(x)
    for i in range(len(x)):
        b[i]=a[i][1]
        
    c=[0]*len(x)
    for i in range(len(x)):
        c[b[i]]=i+1

    return c

def mixed_alphabet(keyword, combined=False):
    kw_alphabet_added = keyword.upper() + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if combined:
        kw_alphabet_added = kw_alphabet_added.replace("J","I")

    already_appeared=[]
    result =""
    for s in kw_alphabet_added:
        if not s in already_appeared:
            result+=s
            already_appeared.append(s)
    return result

def unique(text):
    already_appeared=[]
    result =""
    for s in text:
        if not s in already_appeared:
            result+=s
            already_appeared.append(s)
    return result

def mixed_alphanumeric(keyword):
    kw_alphabet_added = keyword.upper() + "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return unique(kw_alphabet_added)

def replace_all_words(text, dic):
    #this may be fast, but if the words after conversion is included in the map_from table, duplicatedly affected and get wrong. 
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

def replace_all(text, table_from, table_to):
    result =''
    for s in text:
        if s in table_from:
            result += table_to[table_from.find(s)]
        else:
            result += s
    return result

def split_by_len(text, length):
    return [text[i:i+length] for i in range(0,len(text),length)]

def extract_integer_only(text):
    import re
    return re.sub('\\D', '', text)



