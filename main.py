import numpy as np
import matplotlib.pyplot as plt
from random import randint


def variation(x, y):
    return x, y


def transform(x, y, i, img):
    if i == 0:
        img[int(x), int(y)] = 1
        return x, y
    else:
        tx = np.array([[1/2, 0, 0],
                       [1/2, 0, 1/2],
                       [1/2, 0, 0]])

        ty = np.array([[0, 1/2, 0],
                       [0, 1/2, 0],
                       [0, 1/2, 1/2]])
        print(i)
        x, y = transform(x, y, i - 1, img)
        img[int(x), int(y)] = 1
    return (tx[i, 0] * x) + (tx[i, 1] * y) + tx[i, 2], (ty[i, 0] * x) + (ty[i, 1] * y) + ty[i, 2]


def post_transform(x, y):
    return x, y


if __name__ == '__main__':
    ITERS = 50
    SIZE_X = 100
    SIZE_Y = 100

    fractal = np.zeros((SIZE_X, SIZE_Y))

    fig = plt.figure(frameon=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.tick_params(which='both', bottom=0, top=0, labelbottom=0, left=0, right=0, labelleft=0)
    ax.set_xlim(0, SIZE_X); ax.set_ylim(0, SIZE_Y)

    x, y = transform(fractal.shape[0] - 1, fractal.shape[1] - 1, 2, fractal)

    plt.imshow(fractal, cmap='gray')
    plt.show()
