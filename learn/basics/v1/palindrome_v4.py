if __name__ == "__main__":
    a = str(input("Enter a word:"))

    if a[:] == a[::-1]:
        print("Given string is Palindrome!")
    else:
        print("Given string is NOT a Palindrome!")