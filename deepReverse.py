#   deepReverse(L) takes as input a list of elements where some of those elements may be lists themselves.
#   deepReverse returns the reversal of the list where, additionally, any element that is a list is also deepReversed.

def deepReverse(L):
    newList = []
    for i in range(len(L)-1,-1,-1):
        if type(L[i]) == type([1, 2, 3]):
            newList.append(deepReverse(L[i]))
        else:
            newList.append(L[i])
    return newList

print deepReverse([1, 2, 3])
print deepReverse([1, [2, 3], 4])
print deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]])
print deepReverse([10,9,8,[7,[6,5,[4,3,2,[1]]]]])

