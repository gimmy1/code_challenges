"""
Largest Non-repeating substring
"""
def largest_nonrepeating_substring(string):
    lastSeen = {}
    longest = ""
    curr = ""
    startIdx = 0
    for i, char in enumerate(string):
        import pdb; pdb.set_trace()
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

print(largest_nonrepeating_substring("calementisacap"))