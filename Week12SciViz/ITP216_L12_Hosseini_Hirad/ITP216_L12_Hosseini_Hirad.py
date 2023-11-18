# Hirad Hosseini, hiradhos@usc.edu
# ITP 216, Fall 2023
# Section: 32081
# Lab 12
# Description:
# Describe what this program does in your own words such as:
'''
This program uses our newly learned concepts underlying numpy and matplotlib in order to make a simple visualization of
various trigonometric functions.
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.arange(-np.pi, np.pi, 0.1)

    y = np.sin(x)
    fig, ax = plt.subplots(2,3)
    ax[0,0].plot(x, y)
    ax[0,0].set(title = "sin(x)", xlabel = "x", ylabel = "y")

    y2 = np.cos(x)
    ax[0,1].plot(x,y2)
    ax[0,1].set(title = "cos(x)", xlabel = "x", ylabel="y")

    y3 = np.tan(x)
    ax[0, 2].plot(x, y3)
    ax[0, 2].set(title="tan(x)", xlabel="x", ylabel="y")

    y4 = np.sinh(x)
    ax[1, 0].plot(x, y4)
    ax[1, 0].set(title="sinh(x)", xlabel="x", ylabel="y")

    y5 = np.cosh(x)
    ax[1, 1].plot(x, y5)
    ax[1, 1].set(title="cosh(x)", xlabel="x", ylabel="y")

    y6 = np.tanh(x)
    ax[1, 2].plot(x, y6)
    ax[1, 2].set(title="tanh(x)", xlabel="x", ylabel="y")

    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()