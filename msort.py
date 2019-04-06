def msort(iterable):
    return _msort(list(iterable))

def _msort(iterable):
    if len(iterable) <= 1:
        return iterable

    middle = len(iterable) // 2

    left, right = _msort(iterable[:middle]), _msort(iterable[middle:])

    return merge(left, right)

def merge(left, right):
    result = []

    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    result.extend(left + right)

    return result
