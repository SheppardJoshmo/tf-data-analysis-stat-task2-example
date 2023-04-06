import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 696934164 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import chi2
    a = 0
    theta = 0
    n = len(x)
    c_1 = chi2.ppf(p/2, n - 1)
    c_2 = chi2.ppf(1 - p/2, n - 1)
    s2 = np.var(x, ddof=1)
    theta_left = np.sqrt((n - 1) * s2 / c_2)
    theta_right = np.sqrt((n - 1) * s2 / c_1)
    return theta_left, theta_right
