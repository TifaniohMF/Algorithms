import pytest
from src.cos import cos

def test_cos():
	assert cos(0, in_degrees=True) == 1
	assert cos(180, in_degrees=True) == -1
	assert cos(5, in_degrees=True) == 0.9961946980917454