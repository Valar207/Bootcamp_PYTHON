t = (19,42,21,59,36,1,0,23)

res = ""
i = 0

if (len(t) > 1):
    res = "The " + str(len(t)) + " numbers are: "
while i < len(t):
    if i != len(t) - 1:
        res += str(t[i]) + ", "
    else:
        res += str(t[i])
    i += 1
print(res)