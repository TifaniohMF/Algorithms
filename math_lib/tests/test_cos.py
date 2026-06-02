import pytest
from src.cos import *

def test_cos():
	assert cosinus(0).cos(in_degrees=True) == 1
	assert cosinus(180).cos(in_degrees=True) == -1
	assert cosinus(5).cos(in_degrees=True) == 0.9961946980917454