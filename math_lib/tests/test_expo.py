import pytest
from src.expo import *

def test_exp():
	assert expo(1).exp() == 2.7182818284590455
	assert expo(5).exp() == 148.41315910257657
