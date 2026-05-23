import pytest
from src.factorial import *

def test_fact():
	assert facto.fact(4) == 24
	assert facto.fact(30) == 265252859812191058636308480000000