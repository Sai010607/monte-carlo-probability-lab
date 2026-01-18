def uniform_theory():
    return {
        "mean": 0.5,
        "variance": 1/12,
        "prob_gt_0_7": 0.3
    }

def normal_theory():
    return {
        "mean": 0,
        "variance": 1,
        "prob_abs_lt_1": 0.6827
    }

def poisson_theory(lam):
    return {
        "mean": lam,
        "variance": lam
    }

def exponential_theory(lam):
    return {
        "mean": 1/lam,
        "variance": 1/(lam**2)
    }
