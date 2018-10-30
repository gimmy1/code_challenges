"""
Largest Palindromic Substring
"""

def largest_palindromic_substring(string):
    current = [0,1]
    for i in range(len(string)):
        odd = get_largest_palindrome(string, i-1, i+1)
        even = get_largest_palindrome(string, i-1, i)
        largest = max(odd, even, lambda x: x[1] - x[0])
        current = max(current, largest, lambda x: x[1] - x[0])

    return string(currentcurrent[0], current[1])


def get_largest_palindrome(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left -= 1
        right += 1
    
    return [left + 1, right]