import sys
import string

av1 = sys.argv[1]
av2 = sys.argv[2]
if (len(sys.argv) == 3 and av2.isdigit() == True and av1.isdigit() == False):
    av2 = int(sys.argv[2]) 
    l = av1.translate(str.maketrans("","", string.punctuation)).split()
    l = [elem for elem in l if len(elem) > av2]
    print(l)
else:
    print("ERROR")