import sys

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("Put one argument")
    elif len(args) > 1:
        print("AssertionError: more than one argument is provided")
    elif len(args) == 1:
        if args[0].isdigit() == False:
           print("AssertionError: argument is not an integer")
           sys.exit()
        if int(args[0]) == 0:
            print("I'm Zero.")
        elif int(args[0]) % 2 == 0:
            print("I'm Even.")
        elif int(args[0]) % 2 != 0:
            print("I'm Odd.")

    sys.exit()



if __name__=="__main__":
    main()
