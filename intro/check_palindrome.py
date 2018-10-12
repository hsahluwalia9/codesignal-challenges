def check_palindrome(input_string):
    input_string_no_spaces = input_string.replace(" ", "")
    if input_string_no_spaces == input_string_no_spaces[::-1]:
        return True
    return False