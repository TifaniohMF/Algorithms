import pytest
import numpy as np
from main import *

def test_simplex_method():
    '''
    MAXIMIZATION
    Maximize Z = 3x1 + 2x2
    Under contraint
    2x1 + 1x2 <= 18
    2x1 + 3x2 <= 42
    3x1 + 1x2 <= 24
    '''
    c_max = [3, 2]
    A_max = [[2, 1],[2, 3],[3, 1]]
    b_max = [18, 42, 24]

    solveur_max = Simplex(c_max, A_max, b_max, opt_type='max')
    sol_max, z_max = solveur_max.solve()
    
    np.testing.assert_array_equal(sol_max, np.array([3., 12.]))
    assert z_max == 33.0
   
    '''
	MINIMIZATION
	Minimize Z = 20x1 + 40x2
	Under contraint 
	2x1 + 1x2 <= 16
	1x1 + 1x2 <= 12
	1x1 + 3x2 <= 18
	'''
    c_min = [-20, -40]
    A_min = [
        [2, 1],
        [1, 1],
        [1, 3]
    ]
    b_min = [16, 12, 18]

    solveur_min = Simplex(c_min, A_min, b_min, opt_type='min')
    sol_min, z_min = solveur_min.solve()
    
    np.testing.assert_array_equal(sol_min, np.array([6., 4.]))
    assert z_min == 280
