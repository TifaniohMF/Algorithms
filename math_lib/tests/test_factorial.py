import pytest
from src.factorial import *

def test_fact():
	assert factorial(4).fact() == 24
	assert factorial(30).fact() == 265252859812191058636308480000000
