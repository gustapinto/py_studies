''' Some examples of operations with data structures '''

''' Dictionaries '''

# Dictionaries store data and objects each identified with a key
# they allow a more efficient data lookup, insertion and deletion

py_dictionary = {
    'key1': 'some data, in this case a string',
    'key2': 4002,
    'key3': 8922,
}

print(f'''
Operations with Dictionaries

Dictionary key1 data: {py_dictionary['key1']}
''')

''' Lists '''

# List store data in a ordered way, without a key binding
# thay are the python mutable dynamic arrays

py_list = ['cléber', 'clébinho', 'clébson', 'cléber']

print(f'''
Operations with Lists

Count cléber: {py_list.count('cléber')}
Index of clébinho: {py_list.index('clébinho')}
Reverse: {py_list.reverse(), py_list}
Append clébão: {py_list.append('clebão'), py_list}
Sort: {py_list.sort(), py_list}
Copy: {py_list.copy()}
''')

''' Tuples '''

# Tuples are the python immutable array like structure
# they support most of the list operations, excluding the mutable ones

py_tuple = ('some data', 'another data', 'something else data')

print(f'''
Operations with Tuples

Count some data: {py_tuple.count('some data')}
Index of another data: {py_tuple.index('another data')}
''')
