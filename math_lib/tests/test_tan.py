import pytest
from src.tan import *

def test_tan():
	assert tangent(10).tan(in_degrees=True) == 0.17632698070846495
	assert tangent(0).tan(in_degrees=True) == 0
	assert tangent(100).tan(in_degrees=True) == -5.67128181961771
