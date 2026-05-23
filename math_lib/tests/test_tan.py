import pytest
from src.tan import *

def test_tan():
	assert tangent.tan(10, in_degrees=True) == 0.17632698070846495
	assert tangent.tan(0, in_degrees=True) == 0
	assert tangent.tan(100, in_degrees=True) == -5.67128181961771