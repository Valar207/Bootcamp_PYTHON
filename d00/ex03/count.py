import string

def text_analyzer(str = ""):
    "This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."
    if str == "":
        str = input("What is the text to analyse?\n")
    characters = sum(1 for letter in str)
    upper = sum(1 for letter in str if letter.isupper())
    lower = sum(1 for letter in str if letter.islower())
    punctuation = sum(1 for punc in str if punc in string.punctuation)
    spaces = sum(1 for space in str if space.isspace())
    print("The text contains {} characters" . format(characters))
    print("- {} upper letters". format(upper))
    print("- {} lower letters". format(lower))
    print("- {} punctuation marks". format(punctuation))
    print("- {} spaces". format(spaces))