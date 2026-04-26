import pytest
from src.abs import *

def test_abs():
	assert abs(-2) == 2
	assert abs(10) == 10
	assert abs(-100) == 100
	
def test_absMax():
	assert absMax([1,4,6,-11]) == -11
	assert absMax([1,6,7,25]) == 25
	assert absMax([-1,-3,-7,-100]) == -100
	
def test_absMin():
	assert absMin([-1,4,6,-11]) == -1
	assert absMin([19,6,7,25]) == 6
	assert absMin([-9,-3,-7,-100]) == -3