"""Statistical utilities: 95% t-confidence intervals and paired tests."""
import numpy as np
from scipy import stats as sps


def mean_ci95(x):
    x = np.asarray(x, dtype=float)
    n = x.size
    if n < 2:
        return float(x.mean()) if n else 0.0, 0.0
    m = float(x.mean())
    half = float(sps.t.ppf(0.975, df=n - 1) * x.std(ddof=1) / np.sqrt(n))
    return m, half


def wilcoxon_paired(x, y, alternative="two-sided"):
    """Wilcoxon signed-rank test on paired samples; returns (stat, p)."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    diff = x - y
    if np.allclose(diff, 0):
        return 0.0, 1.0
    res = sps.wilcoxon(x, y, alternative=alternative,
                       zero_method="wilcox", method="approx")
    return float(res.statistic), float(res.pvalue)