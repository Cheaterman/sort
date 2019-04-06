from sort import swap

def bsort(iterable):
    return _bsort(list(iterable))

def _bsort(iterable):
    while True:
        swapped = False

        for index in range(0, len(iterable) - 1, 1):
            if iterable[index] > iterable[index + 1]:
                swap(iterable, index, index + 1)
                swapped = True

        if not swapped:
            return iterable
