from src.tan import tan

def test_tan():
	assert tan(10, in_degrees=True) == 0.17632698070846495
	assert tan(0, in_degrees=True) == 0
	assert tan(100, in_degrees=True) == -5.67128181961771