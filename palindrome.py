"""
Check is a word or sentence is a palindrome
"""


def palindrome(input):
    original_input = input.replace(" ", "")
    output = original_input[::-1].replace(" ", "")

    if original_input == output:
        print("Its a palindrome")
    else:
        print("Not a palindrome")


if __name__ == '__main__':
    palindrome_check = input("Enter a word: ")
    palindrome(palindrome_check)
