import sys

Morse = {"A" : ".-",   "B"  : "-...", "C"  : "-.-.", "D"  : "-..",
        "E"  : ".",    "F"  : "..-.", "G"  : "--.",  "H"  : "....",
        "I"  : "..",   "J"  : ".---", "K"  : "-.-",  "L"  : ".-..",
        "M"  : "--",   "N"  : "-.",   "O"  : "---",  "P"  : ".--.",
        "Q"  : "--.-", "R"  : ".-.",  "S"  : "...",  "T"  : "-",
        "U"  : "..-",  "V"  : "...-", "W"  : ".--",  "X"  : "-..-",
        "Y"  : "-.--", "Z"  : "--..",
        "1"  : ".----", "2" : "..---", "3" :  "...--",
        "4"  : "....-", "5" : ".....", "6" : "-....",
        "7"  : "--...", "8" : "---..", "9" : "----.",
        "0"  : "-----", " " : "/"
        }

def main():
    args = sys.argv[1:]

    if len(args) < 1:
        print("Put at least 1 argument")
        return

    line_to_change = ""
    for arg in args:
        for elem in arg:
            if elem != " " and elem.isalnum() == False:
                print("Only alphanumeric values or spaces")
                return
        line_to_change += arg + " "
       
    line_to_change = line_to_change.rstrip(" ")
    line_to_change = line_to_change.upper()
    print("[" + line_to_change + "]")
    for letter in line_to_change:
        if letter in Morse:
            print(Morse[letter], end='')
            print(" ", end='')

    print("")    



if __name__=="__main__":
    main()
