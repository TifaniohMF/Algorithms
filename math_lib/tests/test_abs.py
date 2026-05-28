import pytest
from src.abs import *

def test_abs():
	m1 = absolute(-2)
	m2 = absolute(10)
	m3 = absolute(-100)
	assert m1.abs() == 2
	assert m2.abs() == 10
	assert m3.abs() == 100
	
def test_absMax():
	m4 = absolute([1,4,6,-11])
	m5 = absolute([1,6,7,25])
	m6 = absolute([-1,-3,-7,-100])
	assert m4.absMax() == 11
	assert m5.absMax() == 25
	assert m6.absMax() == 100
	
def test_absMin():
	m7 = absolute([-1,4,6,-11]) 
	m8 = absolute([19,6,7,25])
	m9 = absolute([-9,-3,10,-15])
	assert m7.absMin() == -1
	assert m8.absMin() == 6
	assert m9.absMin() == 3