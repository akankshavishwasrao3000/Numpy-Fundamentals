'''
# Time comparison using %timeit
# %timeit  → measures one line
# %%timeit → measures the entire cell

import timeit
import numpy as np

%timeit [j**4 for j in range(1, 9)]     # Python list
%timeit np.arange(1, 9)**4              # NumPy array



Output: 
1.2 µs ± 0.05 µs per loop (1,000,000 loops)
600 ns ± 20 ns per loop (1,000,000 loops)

'''