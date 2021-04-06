import numpy as np
import pandas as pd
import tensorflow as tf

ar = np.array([1, 2, 3])

print(ar)

def sigmoid(x):
    return 1 / (1+ np.exp(-x))

