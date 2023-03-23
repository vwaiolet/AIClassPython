def palindrome(word):
    word = word.lower()
    word = word.replace(' ', '')
    if word == word[::-1]:
        return True
    else:
        return False


print(palindrome('anna'))
print(palindrome('banana'))
print(palindrome('Anna'))
print(palindrome('My gym'))
