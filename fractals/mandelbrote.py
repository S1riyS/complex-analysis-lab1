import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n


def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    return (r1, r2, np.array([[mandelbrot(complex(r, i), max_iter) for r in r1] for i in r2]))


def display_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1, r2, mandelbrot_array = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot_array, extent=(xmin, xmax, ymin, ymax), cmap="hot")
    plt.colorbar()
    plt.title(f"Mandelbrot Set (Max Iterations: {max_iter})")
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.show()


# Parameters for the Mandelbrot set
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 200

# Display the Mandelbrot set
display_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
