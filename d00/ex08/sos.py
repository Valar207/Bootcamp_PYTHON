import sys

if (len(sys.argv) < 2):
    exit(0)
sys.argv.pop(0)

for i in sys.argv:
    for le in i:
        if (le.isnumeric() is False and le.isalpha()
                is False and le.isspace() is False):
            print("ERROR")
            exit(0)

else:
    morse = {'A': '.-', 'B': '-...',
             'C': '-.-.', 'D': '-..', 'E': '.',
             'F': '..-.', 'G': '--.', 'H': '....',
             'I': '..', 'J': '.---', 'K': '-.-',
             'L': '.-..', 'M': '--', 'N': '-.',
             'O': '---', 'P': '.--.', 'Q': '--.-',
             'R': '.-.', 'S': '...', 'T': '-',
             'U': '..-', 'V': '...-', 'W': '.--',
             'X': '-..-', 'Y': '-.--', 'Z': '--..',
             '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....',
             '7': '--...', '8': '---..', '9': '----.',
             '0': '-----', ' ': '/'}

    for i in sys.argv:
        le = [el for el in sys.argv]

    le = [' '.join(i.split()).upper() for i in sys.argv]
    res = ""
    for strr in le:
        for c in strr:
            res += morse[c] + ' '
        res += '/ '
    res = res[:-2]
    print(res)
