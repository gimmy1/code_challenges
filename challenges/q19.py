"""
Return all keys whose value is passed in target
Nested Dictionary

Example: 
Dictionary => {'a': 2,'b': {'c': 2,'d': { 'e': 2 }}}
Output => [['a'], ['b', 'c'], ['b', 'd', 'e']]

"""
from collections import Mapping
def find_all_keys(dictionary, target, *args):
    values = []
    import pdb; pdb.set_trace()
    for key in dictionary:
        if dictionary[key] == target:
            if args:
                for arg in args:
                    values.append(arg)
                values[0].extend([key])
            else:
                values.append([key])
        elif isinstance(dictionary[key], Mapping): # or dict
            if args:
                values.extend(find_all_keys(dictionary[key], target, values[0][:-1], key))
            else:
                values.extend(find_all_keys(dictionary[key], target, key))
        
    return values

    

dict_1 = {'a': 2,'b': {'c': 2,'d': { 'e': 2 }}}
print(find_all_keys(dict_1, 2)) # => [['a'], ['b', 'c'], ['b', 'd', 'e']]

