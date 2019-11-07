import sys
import string


if (len(sys.argv) == 3 and sys.argv[2].isdigit()
        is True and sys.argv[1].isdigit() is False):
    av1 = sys.argv[1]
    av2 = int(sys.argv[2])
    le = av1.translate(str.maketrans("", "", string.punctuation)).split()
    le = [elem for elem in le if len(elem) > av2]
    print(le)
else:
    print("ERROR")
