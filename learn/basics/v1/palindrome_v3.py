def reverse(word):
    x = ''
    for i in range(len(word)):
        x += word[len(word) - 1 -i]
    return str(x)

word = input("Please type a word:")
x = reverse(word)
print("reverse word:" + x)
if x == word:
    print("Given string is Palindrome!")
else:
    print("Given string is NOT a Palindrome!")