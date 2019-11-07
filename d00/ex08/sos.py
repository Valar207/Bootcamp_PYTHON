import sys

if (len(sys.argv) < 2):
    exit(0)
sys.argv.pop(0)

for i in sys.argv:
    for l in i:
        if (l.isnumeric() == False and l.isalpha() == False and l.isspace() == False):
            print("ERROR")
            exit(0)

else:
    morse ={'A':'.-', 'B':'-...', 
            'C':'-.-.', 'D':'-..', 'E':'.', 
            'F':'..-.', 'G':'--.', 'H':'....', 
            'I':'..', 'J':'.---', 'K':'-.-', 
            'L':'.-..', 'M':'--', 'N':'-.', 
            'O':'---', 'P':'.--.', 'Q':'--.-', 
            'R':'.-.', 'S':'...', 'T':'-', 
            'U':'..-', 'V':'...-', 'W':'.--', 
            'X':'-..-', 'Y':'-.--', 'Z':'--..', 
            '1':'.----', '2':'..---', '3':'...--', 
            '4':'....-', '5':'.....', '6':'-....', 
            '7':'--...', '8':'---..', '9':'----.', 
            '0':'-----', ' ': '/'} 

    for i in sys.argv:
        l = [el for el in sys.argv]

    l = [' '.join(i.split()).upper() for i in sys.argv]
    res = ""
    for strr in l:
        for c in strr:
            res += morse[c] + ' '
        res += '/ '
    res = res[:-2]
    print(res)