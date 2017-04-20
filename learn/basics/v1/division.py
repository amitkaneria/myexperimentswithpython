if __name__ == "__main__":
    while True:
        ins = int(input("Enter a number (-1 to exit) :"))

        if ins == -1:
            exit()

        newList = [1,]
        rangeList = range(2, ins-1)
        for i in rangeList:
            if ins%i == 0:
                newList.append(i)
            i = i+1

        newList.append(ins)
        print(newList)