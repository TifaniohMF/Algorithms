import pytest
from src.stats import *

def test_sum():
	assert Stats.sum([1,2,3,4]) == 10
	assert Stats.sum([10,20,20]) == 50
	assert Stats.sum([1.5,2.5,3]) == 7
	
def test_mean():
	assert Stats.mean([2,3,4,7]) == 4
	assert Stats.mean([20,20,20]) == 20
	assert Stats.mean([1,6]) == 3.5
	
def test_var():
	assert Stats.var([2,3,4,7]) == 3.5
	assert Stats.var([20,20,20]) == 0
	
def test_ecart():
	assert Stats.ecart([20,20,20]) == 0
	assert Stats.ecart([2,4,6,8]) == 2.23606797749979