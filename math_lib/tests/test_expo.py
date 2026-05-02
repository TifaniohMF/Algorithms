import pytest
from src.expo import *

def test_exp():
	assert exp(1) == 2.7182818284590455
	assert exp(5) == 148.41315910257657