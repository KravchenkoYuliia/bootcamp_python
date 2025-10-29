import sys
import string

def get_result(line, nb):
    
    result = ""
    parts_of_line = line.split(" ")

    for word in parts_of_line:

        punct_nb = 0
        for sign in string.punctuation:
            punct_nb += word.count(sign)

        non_punct = len(word) - punct_nb
        if non_punct > int(nb):
            result += word + " "
    
    return result.rstrip(" ")

def right_format(line):

    for sign in string.punctuation:
        line = line.replace(sign, "")
    
    result = line.split(" ")
    return result

def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print("Put 2 argument")
        return 
    elif args[0].isdigit() == True:
        print ("First argument must be a string")
        return 
    elif args[1].isdigit() == False:
        print ("Second argument must be an integer")
        return
    
    result = get_result(args[0], args[1])
    result = right_format(result)

    print(result)


if __name__=="__main__":
    main()
