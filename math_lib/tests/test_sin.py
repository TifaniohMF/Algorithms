import pytest
from src.sin import sin

def test_sin():
	assert sin(0, in_degrees=True) == 0
	assert sin(90, in_degrees=True) ==  1.0000000000000002
	assert sin(10, in_degrees=True) == 0.17364817766693033