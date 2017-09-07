#!/usr/bin/env python
import numpy as np

# Create some data
array = np.arange(16).reshape(-1, 2)
array

# View every row and all columns before one - so the first column number zero
print(array[:, :1])
# View every row/column
print(array[:, ])
