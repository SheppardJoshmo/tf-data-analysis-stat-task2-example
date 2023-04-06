import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 696934164 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    import pandas as pd
    import numpy as np
    from scipy.stats import chi2
    a = 1 - p
    n = len(x)
    s2 = np.sum(x**2)
    c_1 = chi2.ppf(a/2, 2 * n)
    c_2 = chi2.ppf(1 - a/2, 2 * n)
    left = np.sqrt(s2 / (c_2 * 34))
    right = np.sqrt(s2 / (c_1 * 34))
    return left, right
