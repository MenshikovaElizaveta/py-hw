import pytest
from sort import Sort
from conftest import random_n


"""обычные unit тесты + крайние случаи"""

@pytest.mark.parametrize(
	["arr", "the_correct_order"], [
		([10000, 823, 23, 1, 90, 3], [1, 3, 23, 90, 823, 10000]),
		([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
		([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
		([7, 7, 7, 7, 7], [7, 7, 7, 7, 7])
	]
)


def test_sort1(arr, the_correct_order):
	assert Sort(arr) == the_correct_order


"""property based тесты с другими реализованными сортировками"""

def test_sort2(random_n):
	assert Sort(random_n) == sorted(random_n)
