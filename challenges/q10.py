"""Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false."""
def balanced_brackets(expression):
    mapping = dict(zip('([{', ')]}'))
    import pdb; pdb.set_trace()
    queue = []
    for letter in expression:
        if letter in mapping:
            queue.append(mapping[letter])
        elif not queue or letter != queue.pop():
            return False
    return not queue
