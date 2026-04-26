import pytest
from fibonacci import *

def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(15) == 610