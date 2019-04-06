from sort import swap

def isort(iterable):
    return _isort(list(iterable))

def _isort(iterable):
    for index in range(len(iterable)):
        for other_index in range(index - 1, -1, -1):
            index = other_index + 1
            current_value = iterable[index]
            other_value = iterable[other_index]

            if current_value > other_value:
                break

            swap(iterable, index, other_index)

    return iterable
