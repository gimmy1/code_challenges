"""
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.
"""
def reverse(string):
    left = 0
    right = len(string)-1
    string_list = list(string)
    while left < right:
        import pdb; pdb.set_trace()
        if not isalphabet(string_list[left]):
            left += 1
        elif not isalphabet(string_list[right]):
            right -= 1
        else:
            string_list[left], string_list[right] = string_list[right], string_list[left]
            left += 1
            right -= 1
    
    return ''.join(string_list)


def isalphabet(char):
    return char.isalpha()



print(reverse("Ab,c,de!$"))