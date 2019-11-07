import sys

if (len(sys.argv) == 3):
    if (sys.argv[1].isnumeric() is True and sys.argv[2].isnumeric() is True):
        somme = int(sys.argv[1]) + int(sys.argv[2])
        diff = int(sys.argv[1]) - int(sys.argv[2])
        product = int(sys.argv[1]) * int(sys.argv[2])
        if (int(sys.argv[2]) == 0):
            quotient = "ERROR (div by zero)"
            remainder = "ERROR (modulo by zero)"
        else:
            quotient = int(sys.argv[1]) / int(sys.argv[2])
            remainder = int(sys.argv[1]) % int(sys.argv[2])
        print("Sum:         {}" . format(somme))
        print("Difference:  {}" . format(diff))
        print("Product:     {}" . format(product))
        print("Quotient:    {}" . format(quotient))
        print("Remainder:   {}" . format(remainder))
    else:
        print("InputError: only numbers\nUsage: python operations.py\n\
Example:\n    python operations.py 10 3")
elif (len(sys.argv) > 3):
    print("InputError: too many arguments\nUsage: python operations.py\n\
Example:\n    python operations.py 10 3")
elif (len(sys.argv) < 3):
    print("Usage: python operations.py\n\
Example:\n    python operations.py 10 3")
