"""Test of masking of arrays"""
import numpy as np
import numpy.ma as ma
import pandas as pd

np.random.seed(2)
VAL_1 = np.random.normal(1, 2, 100).reshape(100, 1)
VAL_2 = np.random.normal(0, 1, 100).reshape(100, 1)

MASK_1 = VAL_1 > 2

MASK_2 = VAL_1 > VAL_2

VAL_1 = ma.MaskedArray(VAL_1, mask=MASK_1)
VAL_2 = ma.MaskedArray(VAL_2, mask=MASK_2)
VALS = ma.concatenate([VAL_1, VAL_2],axis=1)
# print(VALS)
# quit
D_F = pd.DataFrame(VALS, columns=['First', 'Second']).dropna(axis='index', how='any')
# print(MASK_1)
# print(MASK_2)
print(D_F)
