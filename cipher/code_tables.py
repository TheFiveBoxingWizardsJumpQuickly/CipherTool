def code_table_e(text, table_dict, bin_swap_dict, bin_code=False, delimiter = " "):
    from .common import replace_all
    converted=""

    for s in text[:]:
        if s in table_dict:
            converted+=table_dict[s] + delimiter
        else:
            converted+=s + delimiter
    
    if bin_code:
        converted=replace_all(converted,bin_swap_dict)
    
    return converted

def code_table_d(text, table_dict, bin_swap_dict, bin_code=False, delimiter=" "):
    from .common import replace_all
    if bin_code:
        table_dict_inv = dict((replace_all(j,bin_swap_dict),i) for (i,j) in table_dict.items())
    else:
        table_dict_inv = dict((j,i) for (i,j) in table_dict.items())
    
    code_string = text.split(delimiter)
    converted=""
    for s in code_string:
        if s in table_dict_inv:
            converted+=table_dict_inv[s]
        elif len(s)>0:
            converted+="[" + s + "]"
    
    return converted        




list_A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list_a=list_A.lower()
list_0="0123456789"
list_0_for_atbash="123456789"
list_hex="0123456789abcdef"
list_base36="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
polybius_table = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

morse_code_table = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',  'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 	'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---', '3': '...--',  '4': '....-',  
    '5': '.....', '6': '-....',  '7': '--...',  '8': '---..', '9': '----.', 
    '.' : '.-.-.-', ',' : '--..--', ':' : '---...', '?' : '..--..',
    "'" : '.----.', '-' : '-....-', '/' : '-..-.', '@' : '.--.-.', '=' : '-...-',
    ' ' : '/'
    }
        
bacon1_table = {
    'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
    'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaaa', 
    'K':'abaab', 'L':'ababa', 'M':'ababb', 'N':'abbaa', 'O':'abbab', 
    'P':'abbba', 'Q':'abbbb', 'R':'baaaa', 'S':'baaab', 'T':'baaba', 
    'U':'baabb', 'V':'baabb', 'W':'babaa', 'X':'babab', 'Y':'babba', 'Z':'babbb',
    ' ' : '/'
    }

bacon2_table = {
    'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
    'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
    'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
    'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
    'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab',
    ' ' : '/'
    }

abc012_table = {
    'A':'0', 'B':'1', 'C':'2', 'D':'3', 'E':'4', 
    'F':'5', 'G':'6', 'H':'7', 'I':'8', 'J':'9', 
    'K':'10', 'L':'11', 'M':'12', 'N':'13', 'O':'14', 
    'P':'15', 'Q':'16', 'R':'17', 'S':'18', 'T':'19', 
    'U':'20', 'V':'21', 'W':'22', 'X':'23', 'Y':'24', 'Z':'25',
    ' ' : '/'    
}

#International Radiotelephony Spelling Alphabet (NATO phonetic alphabet)
spelling_alphabet_icao_2008 = {
'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'
}

#1951 ICAO code words
spelling_alphabet_icao_1951 = {
'a':'alfa', 'b':'bravo', 'c':'coca', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'gold', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'metro', 'n':'nectar', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'union', 'v':'victor', 'w':'whiskey', 'x':'extra', 'y':'yankee', 'z':'zulu'
}

#1949 ICAO code words
spelling_alphabet_icao_1949 = {
'a':'alfa', 'b':'beta', 'c':'coca', 'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'julietta', 'k':'kilo', 'l':'lima', 'm':'metro', 'n':'nectar', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 'u':'union', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zebra'
}

#1947 ICAO Latin America/Caribbean
spelling_alphabet_icao_1947_1 = {
'a':'ana', 'b':'brazil', 'c':'coco', 'd':'dado', 'e':'elsa', 'f':'fiesta', 'g':'gato', 'h':'hombre', 'i':'india', 'j':'julio', 'k':'kilo', 'l':'luis', 'm':'mama', 'n':'norma', 'o':'opera', 'p':'peru', 'q':'quebec', 'r':'rosa', 's':'sara', 't':'tomas', 'u':'uruguay', 'v':'victor', 'w':'whiskey', 'x':'equis', 'y':'yolanda', 'z':'zeta'
}

#1947 ICAO alphabet (adopted exactly from ARRL)
spelling_alphabet_icao_1947_2 = {
'a':'adam', 'b':'baker', 'c':'charlie', 'd':'david', 'e':'edward', 'f':'freddie', 'g':'george', 'h':'harry', 'i':'ida', 'j':'john', 'k':'king', 'l':'luis', 'm':'mama', 'n':'norma', 'o':'opera', 'p':'peru', 'q':'quebec', 'r':'rosa', 's':'sara', 't':'tomas', 'u':'uruguay', 'v':'victor', 'w':'whiskey', 'x':'equis', 'y':'yolanda', 'z':'zeta'
}
