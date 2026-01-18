import numpy as np

def uniform_experiment(N=100000):
    samples = np.random.uniform(0, 1, N)
    return samples

def normal_experiment(N=100000):
    samples = np.random.normal(0, 1, N)
    return samples

def poisson_experiment(N=100000, lam=3):
    samples = np.random.poisson(lam, N)
    return samples

def exponential_experiment(N=100000, lam=5):
    samples = np.random.exponential(1/lam, N)
    return samples
