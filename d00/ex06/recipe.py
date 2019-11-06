cookbook = {
    'sandwich' : 
    {
        'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal' : 'lunch',
        'prep_time' : '10'
    },
    'cake' : 
    {
        'ingredients' : ['floar', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'prep_time' : '60'
    },
    'salad': 
    {
        'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal' : 'lunch',
        'prep_time' : '15'
    }
}

for k,v in cookbook.items():
    print(k, v)



