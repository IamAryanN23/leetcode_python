def is_palindrome(x):
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False
# Accept a number from the user
user_input = input("Enter a number: ")
is_palindrome(user_input)

        