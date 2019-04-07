import random
import sort
import timeit

COUNT = 3000
NUMBER = 3
REPEAT = 3

for function in (
    'bsort',
    'gsort',
    'ssort',
    'isort',
    'msort',
    'qsort',
):
    for nature, test_data in {
        'random': [random.random() for _ in range(COUNT)],
        'half ordered': [
            random.random() for _ in range(COUNT // 2)
        ] + list(range(1, COUNT // 2 + 1)),
    }.items():
        assert len(test_data) == COUNT

        print(f'Timing for {function} over {COUNT} {nature} elements:')

        result = min(timeit.repeat(
            f'sort.{function}(test_data)',
            globals=globals(),
            number=NUMBER,
            repeat=REPEAT,
        )) / NUMBER

        result, unit = (
            (result, 'sec')
            if result > 1
            else (result * 1000, 'msec')
        )

        print(f'{NUMBER} loops, best of {REPEAT}: {result:.3g} {unit} per loop\n')
