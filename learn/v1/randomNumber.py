import random

if __name__ == "__main__":
    while True:

        ins = int(input("Enter your number (-1 to exit):"))
        testNum = random.randint(0,10)

        if ins == -1:
            exit()

        while True:
            if ins < testNum:
                ins = int(input("Your number is too LOW, please enter your new number (1-9, -1 to exit):"))
            elif ins > testNum:
                ins = int(input("Your number is too HIGH, please enter your new number (1-9, -1 to exit):"))
            else:
                print("Hurray!, Your magic number is {0}".format(testNum))
                print()
                break
