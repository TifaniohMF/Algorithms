import pytest
from src.sorting_by_bubbles import *
from src.sorting_by_replacement import *
from src.sorting_by_select import *

def test_sort_select():
	assert sort_select([4,3,1,2,5]) == [1,2,3,4,5]
	
def test_sort_remplacement():
    assert sort_replacement([4,3,1,2,5]) == [1,2,3,4,5]

def test_sott_bubbles():
	assert sort_bubbles([4,3,1,2,5]) == [1,2,3,4,5]	