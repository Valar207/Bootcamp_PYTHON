import sys
res = ""
if len(sys.argv) >= 2:
    i = 1
    while i < len(sys.argv):
        res += sys.argv[i] + " "
        i += 1
else:
    exit(0)
print(res.strip().swapcase()[::-1])
