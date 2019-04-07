from collections import deque
from itertools import islice


def msort(iterable):
    return _msort(deque(iterable))

def _msort(iterable):
    msort_stack = deque([iterable])
    merge_stack = deque()

    while True:
        if msort_stack:
            iterable = msort_stack.popleft()

            middle = len(iterable) // 2
            left, right = (
                deque(islice(iterable, 0, middle)),
                deque(islice(iterable, middle, len(iterable))),
            )

            if all(len(side) <= 1 for side in (left, right)):
                merge_stack.extend([left, right])
            else:
                msort_stack.extend([left, right])

        elif len(merge_stack) > 1:
            left, right = merge_stack.popleft(), merge_stack.popleft()
            merge_stack.append(merge(left, right))

        else:
            return list(merge_stack.pop())

def merge(left, right):
    result = deque()

    while left and right:
        if left[0] > right[0]:
            result.append(right.popleft())
        else:
            result.append(left.popleft())

    result.extend(left + right)

    return result
