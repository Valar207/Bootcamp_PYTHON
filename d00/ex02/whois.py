import sys
if len(sys.argv) < 2:
    sys.exit(0)
if (len(sys.argv) > 2 or sys.argv[1].isnumeric() is False):
    print("ERROR")
else:
    if int(sys.argv[1]) == 0:
        print("I'm Zero")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
