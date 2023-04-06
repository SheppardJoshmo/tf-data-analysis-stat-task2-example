import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 696934164 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    from scipy.stats import chi2
    a = 0
    theta = 0
    c_1 = chi2.ppf(p/2, len(x) - 1)
    c_2 = chi2.ppf(1 - p/2, len(x) - 1)
    for elem in x:
        theta = theta + (elem - a)**2
    theta_left = (theta / (34 * c_2))**0.5
    theta_right = (theta / (34 * c_1))**0.5
    return theta_left, theta_right
