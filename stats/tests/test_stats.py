import pytest
from src.stats import *

def test_sum():
	assert Stats([1,2,3,4]).sum() == 10
	assert Stats([10,20,20]).sum() == 50
	assert Stats([1.5,2.5,3]).sum() == 7
	
def test_mean():
	assert Stats([2,3,4,7]).mean() == 4
	assert Stats([20,20,20]).mean() == 20
	assert Stats([1,6]).mean() == 3.5
	
def test_var():
	assert Stats([2,3,4,7]).var() == 3.5
	assert Stats([20,20,20]).var() == 0
	
def test_ecart():
	assert Stats([20,20,20]).ecart() == 0
	assert Stats([2,4,6,8]).ecart() == 2.23606797749979
