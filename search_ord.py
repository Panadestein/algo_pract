"""Search and ordering algorithms"""

# Naive selection sort


def sesort(lst: list) -> list:
    """Selection sort. Very inefficient !!!
    Too lazy to implement a minimum function :))
    List gets modified also in outer scope, so better
    to use the nested for loops"""
    sortl = []
    nnums = len(lst)
    for _ in range(nnums):
        sortl.append(maxi(lst))
        lst.remove(maxi(lst))
    sortl.reverse()  # This can be omitted if one uses min
    return sortl


# A better selection sort


def sesortplus(lst: list) -> list:
    """A more compact selection sort"""
    for idx, _ in enumerate(lst):
        minarg = lst.index(min(lst[idx:]))
        lst[idx], lst[minarg] = lst[minarg], lst[idx]
    return lst


# Quicksort


def qsort(lst: list) -> list:
    """A simple quicksort"""
    if len(lst) < 2:
        return lst
    piv = lst[len(lst) // 2]
    leflist, rightlist = [], []
    lst.remove(piv)
    for elem in lst:
        if elem <= piv:
            leflist.append(elem)
        else:
            rightlist.append(elem)
    return qsort(leflist) + [piv] + qsort(rightlist)


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
    """A recursive binary search"""
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


# Test cases

LST = [22, 333, 4, 55, 66, 0.0001, 33.22]
SRTLST = qsort(LST)
print(SRTLST)
print(binse(333, SRTLST))
print(rebinse(333, SRTLST))
