import sys

def main():
    args = sys.argv[1:]

    if args[0].isdigit() == False or args[1].isdigit() == False:
        print("Wrong argument(s)\nOnly integers are allowed");
        return
    elif len(args) != 2:
        print("Wrong number of arguments\nPut 2 numbers");
        return
    else:
        print("Sum:         [" + str(int(args[0]) + int(args[1])) + "]",
            "\nDifference:  [" + str(int(args[0]) - int(args[1])) + "]",
            "\nProduct:     [" + str(int(args[0]) * int(args[1])) + "]")
        if int(args[1]) == 0:
            print("Quotient:    [error(division by zero)]")
            print("Remainder:   [error(modulo by zero)]")
        else:
            print("Quotient:    [" + str(float(args[0]) / int(args[1])) + "]")
            print("Remainder:   [" + str(int(args[0]) % int(args[1])) + "]")


if __name__=="__main__":
    main()
