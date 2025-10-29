import sys
import string

def text_analyser(text):
    """\n   This function counts the number of upper characters, lower characters,\n   punctuation and spaces in a given text."""
    print("analysing text:", text, "\n")
    
    printable = 0
    upper = 0
    lower = 0
    punctuation = 0
    space = 0

    if isinstance(text, str) == False:
        print("AssertionError: argument is not a string")
        return

    for char in text:
        if char.isprintable() == True:
            printable += 1
            if char == " ":
                space += 1
            if char.isupper() == True:
                upper += 1
            if char.islower() == True:
                lower += 1
            if char in string.punctuation:
                punctuation += 1
    print("The text contains", printable, "printable character(s):\n-", upper, "upper letter(s)\n-", lower, "lower letter(s)\n-", punctuation, "punctuation mark(s)\n-", space, "space(s)")

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Put one argument")
        return
    elif len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return
    text_analyser(args[0])
    sys.exit()

if __name__=="__main__":
    main()
