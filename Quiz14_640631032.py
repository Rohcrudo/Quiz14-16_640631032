# -*- coding: utf-8 -*-
"""

@author: Nattapat Tangniyom 640631032
"""

import numpy as np
from scipy.linalg import solve
A = np.array([[1., 2.], [3., 4.]])
b = np.array([1., 4.])
x = solve(A, b)
print(x)
#[ 2.  -0.5]