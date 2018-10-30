"""Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false."""
def balanced_brackets(expression):
    matching = dict(zip('({[', ')}]'))
    stack = []
    for char in expression:
        import pdb; pdb.set_trace()
        if char in matching:
            stack.append(char)
        elif not stack or matching[stack[-1]] != char:
            return False
        
        if matching[stack[-1]] == char:
            stack.pop()
	
    return len(stack) == 0

print(balanced_brackets("(){}["))