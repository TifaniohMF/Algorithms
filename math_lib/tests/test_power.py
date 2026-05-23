import pytest
from src.power import *

def test_power():
	assert Pow.power(2,2) == 4
	assert Pow.power(3,5) == 243
	assert Pow.power(-3,2) == 9