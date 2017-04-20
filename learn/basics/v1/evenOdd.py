import math

if __name__ == "__main__":
    while True:
        ins = int(input("Enter a number (-1 to exit) :"))
        if ins == -1:
            exit()

        if ins%2 != 0:
            print(str(ins) + " is ODD!")
        else:
            print(str(ins) + " is EVEN!")