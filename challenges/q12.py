"""Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']."""


def original_sentence(phrase, collection):
    reconstructed = []
    for i in range(len(phrase)):
        import pdb; pdb.set_trace()
        if not reconstructed:
            if phrase[len(reconstructed):i+1] in collection:
                # import pdb; pdb.set_trace()
                reconstructed.append(collection[phrase[len(reconstructed):i+1]])
        else:
            if phrase[len(reconstructed[-1]):i+1] in collection:
                # import pdb; pdb.set_trace()
                reconstructed.append(collection[phrase[len(reconstructed[-1]):i+1]])

    return reconstructed or None

print(original_sentence('thequick', {"the":"the", "quick":"quick"}))