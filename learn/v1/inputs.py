from datetime import date

if __name__ == "__main__":
    name = input("Your name, please!")
    age = int(input("Your running year (age +1 ) :"))
    bornYear = date.today().year - age

    print("##############################")
    print("Hi, " + name)
    print(" ... you were born in year:" + str(bornYear))
    print(" ... you will turn 50 years in year:" + str(bornYear + 50))
    print(" ... you will turn 100 years in year:" + str(bornYear + 100))