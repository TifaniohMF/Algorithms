import pytest
from src.sin import *

def test_sin():
	assert sinus.sin(0, in_degrees=True) == 0
	assert sinus.sin(90, in_degrees=True) ==  1.0000000000000002
	assert sinus.sin(10, in_degrees=True) == 0.17364817766693033