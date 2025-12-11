import pytest
import random


@pytest.fixture
def random_numbers():
    arr = []
    for i in range(50):
        a = random.randint(100, 1000)
        arr.append(a)
    return arr
