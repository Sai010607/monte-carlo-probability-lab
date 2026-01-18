import matplotlib.pyplot as plt

def plot_histogram(samples, title, filename):
    plt.hist(samples, bins=100, density=True)
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.savefig(f"results/{filename}")
    plt.close()
