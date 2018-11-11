"""
Return all keys whose value is passed in target
Nested Dictionary

Example: 
Dictionary => {'a': 2,'b': {'c': 2,'d': { 'e': 2 }}}
Output => [['a'], ['b', 'c'], ['b', 'd', 'e']]

"""
from collections import Mapping
def find_all_keys(dictionary, target, *args, **kwargs):
    values = []
    # import pdb; pdb.set_trace()
    inner_values = []
    for key in dictionary:
        if dictionary[key] == target:
            if args:
                for arg in args[0]:
                    inner_values.append(arg)
            elif kwargs:
                inner_values.append(kwargs['key'])
                inner_values.append(key)
                values.append(inner_values)
            else:
                values.append([key])
        elif isinstance(dictionary[key], Mapping): # or dict
            if kwargs:
                arg_list = inner_values[:-1]
                values.extend(find_all_keys(dictionary[key], target, arg_list, key=key))
            else:
                values.extend(find_all_keys(dictionary[key], target, key=key))
        
    return values

    

dict_1 = {'a': 2,'b': {'c': 2,'d': { 'e': 2 }}}
print(find_all_keys(dict_1, 2)) # => [['a'], ['b', 'c'], ['b', 'd', 'e']]

