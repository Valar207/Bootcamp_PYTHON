languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
res = ""
for x in languages:
    res += x + " was created by " + languages[x] + "\n"
res = res.rstrip()
print(res)