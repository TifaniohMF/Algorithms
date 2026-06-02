import pytest
from src.power import *

def test_power():
	assert Pow(2,2).power() == 4
	assert Pow(3,5).power() == 243
	assert Pow(3,2).power() == 9
