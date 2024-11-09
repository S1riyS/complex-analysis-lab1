import matplotlib.pyplot as plt
import numpy as np


def julia(c, max_iter):
    def f(z):
        return z**2 + c

    def julia_set(xmin, xmax, ymin, ymax, width, height):
        r1 = np.linspace(xmin, xmax, width)
        r2 = np.linspace(ymin, ymax, height)
        return (r1, r2, np.array([[iterate(f, complex(r, i), max_iter) for r in r1] for i in r2]))

    def iterate(f, z, max_iter):
        n = 0
        while abs(z) <= 2 and n < max_iter:
            z = f(z)
            n += 1
        return n

    return julia_set


def display_julia(c, xmin, xmax, ymin, ymax, width, height, max_iter):
    r1, r2, julia_array = julia(c, max_iter)(xmin, xmax, ymin, ymax, width, height)
    plt.figure(figsize=(10, 10))
    plt.imshow(julia_array, extent=(xmin, xmax, ymin, ymax), cmap="hot")
    plt.colorbar()
    plt.title(f"Julia Set for c = {c} (Max Iterations: {max_iter})")
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.show()


# Parameters for the Julia set
c = complex(-0.7, 0.27015)  # Change this value to explore different Julia sets
xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
width, height = 800, 800
max_iter = 100

# Display the Julia set
display_julia(c, xmin, xmax, ymin, ymax, width, height, max_iter)
