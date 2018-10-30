"""
Palindrome Check
"""
def palindrome_check(expression):
    for i in range(len(expression) // 2):
        if expression[i] != expression[len(expression) - i -1])]:
            return False
    return True

