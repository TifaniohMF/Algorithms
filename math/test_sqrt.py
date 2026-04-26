import pytest
from src.sqrt import *

def test_sqrt():
	assert sqrt(4) == 2
	assert sqrt(625) == 25
	assert sqrt(10) == 3.1622776601683795
	
def test_sqrt3():
	assert sqrt3(27) == 3
	assert sqrt3(8) == 2