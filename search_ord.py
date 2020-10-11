"""Search and ordering algorithms"""

# Bubble sort


def bubsort(lst: list) -> list:
    """The bubble sort seems to have nothing to recommend it,
    except a catchy name and the fact that it leads
    to some interesting theoretical problems.
    Donald Knuth

    This is only good to check if a list is already sorted.
    """
    swaps = True
    niter = 0
    while swaps:
        swaps = False
        for idx, _ in enumerate(lst[:-niter - 1]):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                swaps = True
        niter += 1
    return lst


# Selection sort


def sesort(lst: list) -> list:
    """Selection sort. Destroys the original list"""
    sortl = []
    nnums = len(lst)
    for _ in range(nnums):
        sortl.append(min(lst))
        lst.remove(maxi(lst))
    return sortl


# A better selection sort


def sesortplus(lst: list) -> list:
    """An improved selection sort (with swapping)"""
    for idx, _ in enumerate(lst):
        minarg = lst.index(min(lst[idx:]))
        lst[idx], lst[minarg] = lst[minarg], lst[idx]
    return lst


# Quicksort


def qsort(lst: list) -> list:
    """A simple quicksort.
    Choosing the pivot is the deal. I have taken
    halve of the array
    """
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


def maxi(lst: list) -> int:
    """Maximum of a list"""
    if len(lst) == 1:
        return lst[0]
    return lst[0] if lst[0] > maxi(lst[1:]) else maxi(lst[1:])


# Loop binary search


def binse(elem: int, lst: list) -> int:
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
ST = bubsort(LST)
print(ST)
#  SRTLST = qsort(LST)
#  print(SRTLST)
#  print(binse(333, SRTLST))
#  print(rebinse(333, SRTLST))
