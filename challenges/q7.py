"""The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them."""

def edit_distance(string1, string2):
    diff = abs(len(string1) - len(string2))
    smaller = min(string1, string2)
    total = 0
    for i in range(len(smaller)):
        if string1[i] != string2[i]:
            total += 1
    
    return total + diff

print(edit_distance('kit', 'sitting'))


