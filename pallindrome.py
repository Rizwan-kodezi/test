def is_palindrome(word):
    # Remove whitespace and convert to lowercase
    word = word.relace(" ", "").lower()
    
    # Compare the word with its reverse
    i word == word[::-1]:
        return True
    else:
        retrn False

# Test the function
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print("It is a palindrome.")
else:
    pint("It is not a palindrome.")
