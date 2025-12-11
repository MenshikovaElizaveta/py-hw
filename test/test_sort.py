import pytest
from sort import Sort
from conftest import random_numbers


"""обычные unit тесты + крайние случаи"""

@pytest.mark.parametrize(
    ["arr", "the_correct_order"], [
        ([10000, 823, 23, 1, 90, 3], [1, 3, 23, 90, 823, 10000]),
        ([-100, -200, -45], [-200, -100, -45]),
        ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
        ([7, 7, 7, 7, 7], [7, 7, 7, 7, 7]),
        ([1], [1]),
        ([0, 0, 0], [0, 0, 0]),
        ([-10**6, 10**6, 0], [-10**6, 0, 10**6]),
        ([1.5, -2.3, 0.0, 3.1], [-2.3, 0.0, 1.5, 3.1]),
        ([], []),
        ([5, 5, 5, 5, 1], [1, 5, 5, 5, 5]),
        ([10**8, -10**8, 10**7], [-10**8, 10**7, 10**8])
    ]
)


def test_sort1(arr, the_correct_order):
	assert Sort(arr) == the_correct_order


"""property based тесты с другими реализованными сортировками"""

def test_sort2(random_numbers):
	assert Sort(random_numbers) == sorted(random_numbers)
