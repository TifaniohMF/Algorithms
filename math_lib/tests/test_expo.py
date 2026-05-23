import pytest
from src.expo import *

def test_exp():
	assert expo.exp(1) == 2.7182818284590455
	assert expo.exp(5) == 148.41315910257657