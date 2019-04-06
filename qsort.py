from sort import swap

def qsort(iterable):
    return _qsort(list(iterable))

def _qsort(iterable, start=0, end=None):
    if end is None:
        end = len(iterable) - 1

    if start >= end:
        return iterable

    new_pivot_index = _partition(iterable, start, end)

    _qsort(iterable, start, new_pivot_index - 1)
    _qsort(iterable, new_pivot_index + 1, end)

    return iterable

def _partition(iterable, start, end):
    pivot, original_pivot_index = _pivot_choice(iterable, start, end)
    pivot_index = start

    for index in range(start, end + 1):
        if(
            index == original_pivot_index
            or iterable[index] > pivot
        ):
            continue

        swap(iterable, pivot_index, index)

        if pivot_index == original_pivot_index:
            original_pivot_index = index

        pivot_index += 1

    swap(iterable, pivot_index, original_pivot_index)

    return pivot_index

def _pivot_choice(iterable, start, end):
    pivot_index = (end - start) // 2 + start
    return (
        iterable[pivot_index],
        pivot_index
    )
