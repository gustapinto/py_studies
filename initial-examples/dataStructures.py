#some examples of operations with data structures

##########################################################################
#lists: aka. dynamic arrays
list = ['cléber', 'clébinho', 'clébson', 'cléber']

def reverse_list(list):
    list.reverse()
    return list

def append_clebao(list):
    list.append('clébão')
    return list

def sort_list(list):
    list.sort()
    return list

print("""
    List Operations

    Count cléber: {count}
    Index of clébinho: {index}
    Reverse: {reverse}
    Append clébão: {append}
    Sort: {sort}
    Copy: {copied_list}
""".format(
    count = list.count('cléber'),
    index = list.index('clébinho'),
    reverse = reverse_list(list),
    append = append_clebao(list),
    sort = sort_list(list),
    copied_list = list.copy(),
))
##########################################################################

##########################################################################
#tuples: aka. fixed boring lists
tuple = ('data1', 'data2', 'data23')
##########################################################################

##########################################################################
#set: unordered data without duplications
set = {'data1', 'data2', 'data1'}

print("""
    Set without duplicated 'data1': {set}
""".format(set = set))
##########################################################################
