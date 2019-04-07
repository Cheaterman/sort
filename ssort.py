from sort import swap

def ssort(iterable):
    return _ssort(list(iterable))

def _ssort(iterable):
    for offset, min_value in enumerate(iterable):
        min_index = offset

        for index, value in enumerate(iterable[offset:]):
            if value < min_value:
                min_index = offset + index
                min_value = value

        swap(iterable, min_index, offset)

    return iterable
