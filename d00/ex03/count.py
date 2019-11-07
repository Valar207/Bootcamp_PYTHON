import string


def text_analyzer(st=""):
    "This function counts the number of upper characters, lower characters,punctuation and spaces in a given text."
    if st == "":
        st = input("What is the text to analyse?\n")
    characters = sum(1 for letter in st)
    upper = sum(1 for letter in st if letter.isupper())
    lower = sum(1 for letter in st if letter.islower())
    punctuation = sum(1 for punc in st if punc in string.punctuation)
    spaces = sum(1 for space in st if space.isspace())
    print("The text contains {} characters" . format(characters))
    print("- {} upper letters". format(upper))
    print("- {} lower letters". format(lower))
    print("- {} punctuation marks". format(punctuation))
    print("- {} spaces". format(spaces))
