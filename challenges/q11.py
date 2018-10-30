"""Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B']."""


def rgb(letters):
    first = letters[0]
    # second = letters[1]
    for i in range(len(letters)):
        if first < letters[i]:
            import pdb; pdb.set_trace()
            swap(first, letters[i])
            break
    return letters

def swap(a, b):
    a, b = b, a

print(rgb(['B', 'G', 'R', 'R', 'B', 'R', 'G']))
