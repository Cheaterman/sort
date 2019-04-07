from sort import swap

def isort(iterable):
    return _isort(list(iterable))

def _isort(iterable):
    for sorted_end in range(1, len(iterable)):
        index = sorted_end - 1
        current_value = iterable[sorted_end]

        for index in range(index, -1, -1):
            value = iterable[index]

            if value < current_value:
                break

            iterable[index + 1] = value

        else:
            if index == 0:
                index = -1

        iterable[index + 1] = current_value

    return iterable
