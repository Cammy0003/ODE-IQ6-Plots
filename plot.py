import matplotlib.pyplot as plt
import numpy as np


def w_1(x):


def w_2(x):
    u_1 = np.zeros_like(x)
    u_1[x >= 1] = 1
    return x - (2*x - 2)*u_1


plt.title(r'Part (a) Plot of $w_1(x)$ and $w_2(x)$')
x_vals = np.linspace(0, 2, 500)
plt.plot(x_vals, -w_1(x_vals), label=r'$w_1(x)$')
plt.plot(x_vals, -w_2(x_vals), label=r'$w_2(x)$')
plt.xlabel("x")
plt.ylabel("w(x)")
plt.legend()

plt.savefig("IQ6_Part_a_plot.png")

plt.show()
