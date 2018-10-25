"""Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle"."""

def create_palindrome(string):
    start = string[0] if string[0] < string[-1] else string[-1]
    
    build_string = ""
    check_palindrome = ""
    if start == string[-1]:
        string = string[::-1]
        build_string += start
        check_palindrome += build_string + string
        if is_palindrome(check_palindrome):
            return check_palindrome
        else:
            check_palindrome = ""
            # import pdb; pdb.set_trace()
            for idx, char in enumerate(string, start=1):
                build_string += string[idx]
                check_palindrome += build_string + string[::-1]
                if is_palindrome(check_palindrome):
                    return check_palindrome
                else: 
                    check_palindrome = ""
    elif start == start[0]:
        build_string += start
        check_palindrome += build_string + string

        if is_palindrome(check_palindrome):
            return check_palindrome
        else: 
            check_palindrome = ""
            for idx, char in enumerate(string, start=1):
                build_string += string[idx]
                check_palindrome += string + build_string[::-1]
                if is_palindrome(check_palindrome):
                    return check_palindrome
                else: 
                    check_palindrome = ""
    return -1

            



def is_palindrome(string):
    return string == string[::-1] # thanks python


print(create_palindrome('elgoog'))
