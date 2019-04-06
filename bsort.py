from sort import swap

def bsort(iterable):
    return _bsort(list(iterable))

def _bsort(iterable):
    for offset in range(0, len(iterable) - 1):
        for index in range(0, len(iterable) - 1 - offset):
            if iterable[index] > iterable[index + 1]:
                swap(iterable, index, index + 1)

    return iterable
