if __name__ == "__main__":
    while True:
        ins = input("Enter a String (-1 to exit):")

        if ins == "-1":
            exit()

        insLength = len(ins)
        flag = False;
        for count in range(int(len(ins)/2)):
            print(ins)
            print(count)
            print(insLength - count + 1)
            if ins[count] == ins[insLength - count - 1]:
                flag = True
            else:
                flag = False
                break

        if flag:
            print("{0} is palindrome!".format(ins))
        else:
            print("{0} is NOT a palindrome!".format(ins))