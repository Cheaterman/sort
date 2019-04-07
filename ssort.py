from sort import swap

def ssort(iterable):
    return _ssort(list(iterable))

def _ssort(iterable):
    for offset in range(len(iterable) - 1):
        min_index = offset

        for index in range(offset, len(iterable)):
            if iterable[index] < iterable[min_index]:
                min_index = index

        swap(iterable, min_index, offset)

    return iterable
