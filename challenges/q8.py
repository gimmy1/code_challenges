"""Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid."""
def encode(string):
    encode = ""
    count = 1
    for i, v in enumerate(string, start=1):
        import pdb; pdb.set_trace()
        if i == len(string):
            encode += str(count) + v
            break
        elif string[i] != string[i-1]:
            encode += str(count) + v
            count = 1
        elif string[i] == string[i-1]:
            count += 1
    return encode

def decode(string):
    decode = ''
    for i in range(len(string) - 1):
        import pdb; pdb.set_trace()
        if string[i].isdigit():
            decode += int(string[i]) * string[i+1]
        else:
            i += 1
    return decode
        

    
# print(encode('AAAABBB'))
print(decode('4A3B'))