import pytest
from src.sqrt import *

def test_sqrt():
	assert Sqrt(4).sqrt() == 2
	assert Sqrt(625).sqrt() == 25
	assert Sqrt(10).sqrt() == 3.1622776601683795
	
def test_sqrt3():
	assert Sqrt(27).sqrt3() == 3
	assert Sqrt(8).sqrt3() == 2
