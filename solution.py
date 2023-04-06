import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 696934164 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import chi2
    n = len(x)
    s2 = 0
    for elem in x:
        s2 = s2 + elem**2
    c_1 = chi2.ppf(p/2, n)
    c_2 = chi2.ppf(1 - p/2, n)
    left = np.sqrt(s2 / (c_2 * 38))
    right = np.sqrt(s2 / (c_1 * 38))
    return left, right
