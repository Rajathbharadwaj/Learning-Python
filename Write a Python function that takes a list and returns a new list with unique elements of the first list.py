
Write a Python function that takes a list and returns a new list with unique elements of the first list.

#CODE
def uni_lst(l):
    return set(l)

#OUTPUT
l = [1,1,1,1,2,2,2,3,3,3,4,4,4]
uni_lst(l)
{1, 2, 3, 4}
    
