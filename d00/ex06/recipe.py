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

choice = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n>> ")

def print_recipe(recip):
    while (recip not in cookbook):
        print("This recipe is not included in this cookbook")
        recip = input("Please enter the recipe's name to get its details:\n>> ")

    print(f"Recipe for {recip}:\nIngredients list: {cookbook[recip]['ingredients']}\nTo be eaten for\
 {cookbook[recip]['meal']}.\nTakes {cookbook[recip]['prep_time']} minutes of cooking.\n")

def add_recip(adrecip, ading, admeal, adprep):
    while (adprep.isdigit() == False):
        adprep = input("You should enter a digit for the preparation time\n >>")
    cookbook.update({adrecip :{'ingredients' : ading, 'meal': admeal, 'prep_time': adprep}})

def remove_recipe(recip):
    if (recip not in cookbook):
        print("\nThis recipe is not int the Cookbook\n")
    else:
        cookbook.pop(recip, None)
        print("\n" + recip + " has been removed successfully\n")

def print_cookbook():
    print("|COOKBOOK|\n")
    for r in cookbook:
        print(f"- {r} -")
        print(f"Ingredients list: {cookbook[r]['ingredients']}\nTo be eaten for\
 {cookbook[r]['meal']}.\nTakes {cookbook[r]['prep_time']} minutes of cooking.\n")

while (choice != "5"):
    while (choice > "5" or choice < "1"):
        choice = input("This option does not exist, please type the corresponding number.\nTo exit, enter 5.\n>>")
    if (choice == "1"):
        adrecip = input("What recipe would you like to add in the CookBook?\n >>")
        ading = input(f"What ingredients does {adrecip} have, separate each ingredient by one space?\n >>")
        ading = list(ading.split())
        admeal = input(f"What kind of meal is {adrecip}?\n >>")
        adprep = input(f"How many minutes is it going to take to prepare {adrecip}?\n >>")
        add_recip(adrecip, ading, admeal, adprep)
    elif (choice == "2"):
        recip = input("\nWhat recipe do you want to remove from the CookBook\n >>")
        remove_recipe(recip)
    elif (choice == "3"):
        recip = input("Please enter the recipe's name to get its details:\n>> ")
        print_recipe(recip)
    elif (choice == "4"):
        print_cookbook()
    choice = input("Please select an option by typing the corresponding number:\
    \n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\
    \n5: Quit\n>> ")

if choice == "5":
    print("Cookbook closed")
    exit(0)