import pytest
from src.sqrt import *

def test_sqrt():
	assert Sqrt.sqrt(4) == 2
	assert Sqrt.sqrt(625) == 25
	assert Sqrt.sqrt(10) == 3.1622776601683795
	
def test_sqrt3():
	assert Sqrt.sqrt3(27) == 3
	assert Sqrt.sqrt3(8) == 2