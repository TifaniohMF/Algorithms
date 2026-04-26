import pytest
from src.power import *

def test_power():
	assert power(2,2) == 4
	assert power(3,5) == 243
	assert power(-3,2) == 9