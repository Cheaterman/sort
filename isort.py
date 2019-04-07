from sort import swap

def isort(iterable):
    return _isort(list(iterable))

def _isort(iterable):
    for sorted_end in range(len(iterable) - 1):
        for index in range(sorted_end, -1, -1):
            if iterable[index] < iterable[index + 1]:
                break

            swap(iterable, index, index + 1)

    return iterable
