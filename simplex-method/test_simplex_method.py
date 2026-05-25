import pytest
import numpy as np
from main import *

def test_simplex_method():
    c_max = [3, 2]
    A_max = [
        [2, 1],
        [2, 3],
        [3, 1]
        ]
    b_max = [18, 42, 24]
    
    solveur_max = Simplex(c_max, A_max, b_max, opt_type='max')
    sol_max, z_max = solveur_max.solve()
    
    np.testing.assert_array_equal(sol_max, np.array([3., 12.]))
    assert z_max == 33.0