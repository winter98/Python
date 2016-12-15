'''
15/12/2016 Cracking the Coding Interview 1.5 One Away

Check if one edit (insert, delete or replace) makes strings match

'''
import math
def insert_delete_test(first, second):
    index = 0

    if len(first) < len(second):
        shorter = list(first)
        longer = list(second)
    else:
        shorter = list(second)
        longer = list(first)

    while index < len(shorter):
        if shorter[index] != longer[index]:
            shorter.insert(index,longer[index])
            return shorter == longer
        index += 1

    return True

def change_one_element(first, second):
    l1 = list(first)
    l2 = list(second)

    index = 0
    while index < len(first):
        if l1[index] != l2[index]:
            l1[index] = l2[index]
            return l1 == l2
        index += 1

    # shouldn't get to here as checked for equivalent earlier .... but
    return True

def compare_string(first, second):
    lengthdiff = abs(len(first) - len(second))
    if lengthdiff > 1:
        return False # can only make one change

    #check for insert / delete
    if lengthdiff == 1:
        return insert_delete_test(first, second)

    # same lengths so check for one diff
    # took out check for equality - doing this in this check now
    return change_one_element(first,second)

def test_it(first, second):
    print("%s, %s -> %s" % (first, second, compare_string(first,second)))

test_it("pale","ple")
test_it("pales","pale")
test_it("pale","bale")
test_it("pale","bake")
