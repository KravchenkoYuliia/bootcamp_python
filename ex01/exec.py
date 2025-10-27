import sys

def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("Put one argument")
        sys.exit()
    elif len(args) != 1:
        concatenated_string = ""
        i = 0
        for arg in args:
            concatenated_string += arg;
            i += 1
            if i < len(args):
                concatenated_string += " "
        string = concatenated_string.swapcase()
    else:
        string = args[0].swapcase()

    print(string[::-1])

    sys.exit()

if __name__=="__main__":
    main()
