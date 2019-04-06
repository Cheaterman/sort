import hypothesis
from hypothesis.strategies import floats, integers, lists, characters
import pytest

import sort


@pytest.fixture(
    params=[sort.qsort, sort.bsort, sort.isort, sort.msort],
    ids=lambda function: f'sort_function={function.__name__}',
)
def sort_function(request):
    return request.param


def max_range_for_function(function):
    max_ranges = {
        sort.bsort: 1000,
        sort.isort: 1000,
    }
    return max_ranges.get(function, 100_000)


@pytest.mark.parametrize(
    'range_max',
    [5, 7, 9, 12, 100, 1000, 10_000, 100_000],
    ids=lambda range_max: f'range_max={range_max}',
)
def test_reversed_list(sort_function, range_max):
    if range_max > max_range_for_function(sort_function):
        pytest.skip(
            f'{sort_function.__name__} is too slow '
            f'to process {range_max} items.'
        )

    test_values = list(reversed(range(range_max)))
    assert sort_function(test_values) == sorted(test_values)


@pytest.mark.parametrize(
    'hypothesis_type',
    [
        lists(integers()),
        lists(floats(allow_nan=False)),
        characters(),
    ],
    ids=lambda types: f'hypothesis_type={types}',
)
def test_hypothesis_type(sort_function, hypothesis_type):
    @hypothesis.given(hypothesis_type)
    def _test_hypothesis_type(test_values):
        assert sort_function(test_values) == sorted(test_values)

    return _test_hypothesis_type()
