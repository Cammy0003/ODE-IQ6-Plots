import matplotlib.pyplot as plt
import numpy as np


def y_1(x):  # w_1
    return (x**2)/48 - (x**3)/48 + (x**4)/192


def y_2(x):  # w_2
    u = np.zeros_like(x)
    u[x >= 1] = 1
    return (x**5)/480 + (5*(x**2))/192 - (x**3)/48 - u * ((x-1)**5)/240


def y_3(x):  # w_3
    u = np.zeros_like(x)
    u[x >= 1] = 1
    return u/24 * ((x-1)**3) + (x**2)/32 - (x**3)/48


plt.title('Part b/c: $y(x)$ under different loads $w_c(x)$')

x_vals = np.linspace(0, 2, 500)
plt.plot(x_vals, -y_1(x_vals), label='with load $w_1$')
plt.plot(x_vals, -y_2(x_vals), label='with load $w_2$')
plt.plot(x_vals, -y_3(x_vals), label='with load $w_3$')

plt.xlabel('$x$')
plt.ylabel('$y(x)$')
plt.legend()

# plt.savefig("IQ6_Part_b_c.png")

plt.show()


