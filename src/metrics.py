from scipy import stats
import numpy as np


def summary_stats(df):
    """Beräknar medelvärde, median, min och max"""
    columns = ["age", "height", "weight", "systolic_bp", "cholesterol"]
    return df[columns].agg(["mean", "median", "min", "max"]).round(2)


def disease_percentage(df):
    """Beräknar andelen personer med sjukdom i procent"""
    return df["disease"].mean() * 100


def blood_pressure_ci(df):
    """Beräknar 95 % konfidensintervall för medelblodtryck"""
    bp = df["systolic_bp"]

    n = len(bp)
    bp_mean = bp.mean()
    bp_std = bp.std(ddof=1)

    se = bp_std / np.sqrt(n)
    z_crit = stats.norm.ppf(0.975)

    low = bp_mean - z_crit * se
    high = bp_mean + z_crit * se

    return bp_mean, low, high


def smoker_bp_difference(df):
    """Beräknar skillnaden i medelblodtryck mellan rökare och icke-rökare"""
    smokers = df.loc[df["smoker"] == "Yes", "systolic_bp"]
    non_smokers = df.loc[df["smoker"] == "No", "systolic_bp"]

    return smokers.mean() - non_smokers.mean()
