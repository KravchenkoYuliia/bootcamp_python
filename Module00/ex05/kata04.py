kata = (0, 4, 132.42222, 10000, 12345.67)


def data_format(index):
   
    result = None

    if int(kata[index]) < 10:
        result = "0" + str(kata[index])
    else:
        result = str(kata[index])
    
    return result


def main():
    
    module = data_format(0)
    ex = data_format(1)

    number1 = f"{float(kata[2]):.2f}"
    number2 = f"{float(kata[3]):.2e}"
    number3 = f"{float(kata[4]):.2e}"
    
    print("module_" + module + ", ex_" + ex, ":", number1 + ",", number2 + ",", number3)


if __name__=="__main__":
    main()
