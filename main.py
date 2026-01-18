import argparse
import numpy as np
from experiments import (
    uniform_experiment,
    normal_experiment,
    poisson_experiment,
    exponential_experiment
)
from theory import (
    uniform_theory,
    normal_theory,
    poisson_theory,
    exponential_theory
)
from plotting import plot_histogram
from logger import log_result


def run_uniform(N):
    samples = uniform_experiment(N)
    theory = uniform_theory()

    mean_est = np.mean(samples)
    var_est = np.var(samples)
    prob_est = np.mean(samples > 0.7)

    print("\n--- Uniform(0,1) ---")
    print("Mean:", theory["mean"], "| Estimated:", mean_est)
    print("Variance:", theory["variance"], "| Estimated:", var_est)
    print("P(X > 0.7):", theory["prob_gt_0_7"], "| Estimated:", prob_est)

    log_result("Uniform(0,1)")
    log_result(f"Mean: {mean_est}")
    log_result(f"Variance: {var_est}")
    log_result(f"P(X > 0.7): {prob_est}")
    log_result("-" * 40)

    plot_histogram(samples, "Uniform(0,1)", "uniform.png")


def run_normal(N):
    samples = normal_experiment(N)
    theory = normal_theory()

    mean_est = np.mean(samples)
    var_est = np.var(samples)
    prob_est = np.mean(np.abs(samples) < 1)

    print("\n--- Normal(0,1) ---")
    print("Mean:", theory["mean"], "| Estimated:", mean_est)
    print("Variance:", theory["variance"], "| Estimated:", var_est)
    print("P(|X| < 1):", theory["prob_abs_lt_1"], "| Estimated:", prob_est)

    log_result("Normal(0,1)")
    log_result(f"Mean: {mean_est}")
    log_result(f"Variance: {var_est}")
    log_result(f"P(|X| < 1): {prob_est}")
    log_result("-" * 40)

    plot_histogram(samples, "Normal(0,1)", "normal.png")


def run_poisson(N, lam):
    samples = poisson_experiment(N, lam)
    theory = poisson_theory(lam)

    mean_est = np.mean(samples)
    var_est = np.var(samples)

    print(f"\n--- Poisson({lam}) ---")
    print("Mean:", theory["mean"], "| Estimated:", mean_est)
    print("Variance:", theory["variance"], "| Estimated:", var_est)

    log_result(f"Poisson({lam})")
    log_result(f"Mean: {mean_est}")
    log_result(f"Variance: {var_est}")
    log_result("-" * 40)

    plot_histogram(samples, f"Poisson({lam})", "poisson.png")


def run_exponential(N, lam):
    samples = exponential_experiment(N, lam)
    theory = exponential_theory(lam)

    mean_est = np.mean(samples)
    var_est = np.var(samples)

    print(f"\n--- Exponential({lam}) ---")
    print("Mean:", theory["mean"], "| Estimated:", mean_est)
    print("Variance:", theory["variance"], "| Estimated:", var_est)

    log_result(f"Exponential({lam})")
    log_result(f"Mean: {mean_est}")
    log_result(f"Variance: {var_est}")
    log_result("-" * 40)

    plot_histogram(samples, f"Exponential({lam})", "exponential.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=str, default="all",
                        help="uniform | normal | poisson | exponential | all")
    parser.add_argument("--N", type=int, default=100000)
    parser.add_argument("--lam", type=float, default=3)

    args = parser.parse_args()

    if args.dist == "uniform":
        run_uniform(args.N)
    elif args.dist == "normal":
        run_normal(args.N)
    elif args.dist == "poisson":
        run_poisson(args.N, args.lam)
    elif args.dist == "exponential":
        run_exponential(args.N, args.lam)
    else:
        run_uniform(args.N)
        run_normal(args.N)
        run_poisson(args.N, args.lam)
        run_exponential(args.N, args.lam)

    print("\nAll experiments completed.")
