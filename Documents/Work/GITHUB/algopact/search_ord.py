"""Search and ordering algorithms"""

# Naive selection sort


def sesort(lst):
    """Selection sort. Very ineffcient !!!
    Too lazy to implement a minimum function :))"""
    sortl = []
    nnums = len(lst)
    for _ in range(nnums):
        sortl.append(maxi(lst))
        lst.remove(maxi(lst))
    sortl.reverse()
    return sortl


# Recursive maximum


def maxi(lst):
    """Maximum of a list"""
    if len(lst) == 1:
        return lst[0]
    return lst[0] if lst[0] > maxi(lst[1:]) else maxi(lst[1:])


# Loop binary search


def binse(elem, lst):
    """A loop binary search"""
    init = 0
    fina = len(lst) - 1
    for _ in lst:
        pos = (init + fina) // 2
        if elem == lst[pos]:
            return pos
        if elem < lst[pos]:
            fina = pos - 1
        if elem > lst[pos]:
            init = pos + 1
    return -1

# Recursive binary search


def rebinse(elem: float, lst: list, initpos: int = 0) -> int:
    """A revursive binary search"""
    pos = len(lst) // 2
    if len(lst) == 1:
        return initpos + pos
    if elem == lst[pos]:
        return initpos + pos
    if elem < lst[pos]:
        return rebinse(elem, lst[:pos], initpos)
    if elem > lst[pos]:
        initpos += pos + 1
        return rebinse(elem, lst[pos + 1:], initpos)
    return -1


# Simple test cases

LST = [22, 333, 4, 55, 66, 0.0001, 33.22]
SRTLST = sesort(LST)
print(SRTLST)
print(binse(333, SRTLST))
print(rebinse(333, SRTLST))
