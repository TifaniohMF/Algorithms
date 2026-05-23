import pytest
from src.abs import *

def test_abs():
	assert absolute.abs(-2) == 2
	assert absolute.abs(10) == 10
	assert absolute.abs(-100) == 100
	
def test_absMax():
	assert absolute.absMax([1,4,6,-11]) == -11
	assert absolute.absMax([1,6,7,25]) == 25
	assert absolute.absMax([-1,-3,-7,-100]) == -100
	
def test_absMin():
	assert absolute.absMin([-1,4,6,-11]) == -1
	assert absolute.absMin([19,6,7,25]) == 6
	assert absolute.absMin([-9,-3,-7,-100]) == -3