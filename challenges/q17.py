"""
Largest Non-repeating substring
"""
def largest_nonrepeating_substring(string):
    lastSeen = {}
    longest = ""
    curr = ""
    startIdx = 0
    for i, char in enumerate(string):
        # import pdb; pdb.set_trace()
        if char in lastSeen:
            if char in curr:
                longest = max(curr, longest)
                startIdx = lastSeen[char]
                curr = string[startIdx+1: i+1]
            else:
                curr += char
        else:
            curr += char
        
        lastSeen[char] = i
    
    return longest

def largest_nonrepeating_substring2(string):
    lastSeen = {}
    longest = [0,1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        import pdb; pdb.set_trace()
        if longest[1] - longest[0] < i+1 - startIdx:
            longest = [startIdx, i+1]
        lastSeen[char] = i
    return string[longest[0]: longest[1]]
            
print(largest_nonrepeating_substring2("clementasa"))