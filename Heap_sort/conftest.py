import pytest
import random

@pytest.fixture
def random_n():
	arr=[]
	for i in range(10):
		a=random.randint(100, 1000)
		arr.append(a)
	return arr
