kata = (2019, 9, 25, 3, 30)

def data_format(index):
   
    result = None

    if int(kata[index]) < 10:
        result = "0" + str(kata[index])
    else:
        result = str(kata[index])
    
    return result


def main():
    
    day = None
    month = None
    year = str(kata[0])
    hour = None
    minute = None

#year
    while len(str(year)) < 4:
        year = "0" + year

    month = data_format(1)
    day = data_format(2)
    hour = data_format(3)
    minute = data_format(4)

    print(month + "/" + day + "/" + year, hour + ":" + minute)
    



if __name__=="__main__":
    main()
