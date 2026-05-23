import pytest
from src.cos import *

def test_cos():
	assert cosinus.cos(0, in_degrees=True) == 1
	assert cosinus.cos(180, in_degrees=True) == -1
	assert cosinus.cos(5, in_degrees=True) == 0.9961946980917454