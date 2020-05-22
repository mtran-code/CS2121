import matplotlib.pyplot as plt
import numpy as np

# Initialize the lists
k = 100
x_list = [x for x in range(1, 1000)]

function_a = [x**2 + 400*x + 5 for x in x_list]
function_b = [67*x + 3*x for x in x_list]
function_c = [2*x + (5*x)*np.log(x) + 100 for x in x_list]
function_d = [np.log(x) + 2*(x**2) + 55 for x in x_list]
function_e = [3*(2**x) + x**8 + 1024 for x in x_list]
function_f = [k*x + np.log(k) for x in x_list]
function_g = [9*x + k*np.log(x) + 1000 for x in x_list]

# Plot the lines
plt.plot(x_list, function_a, label="(a)")
plt.plot(x_list, function_b, label="(b)")
plt.plot(x_list, function_c, label="(c)")
plt.plot(x_list, function_d, label="(d)")
plt.plot(x_list, function_e, label="(e)")
plt.plot(x_list, function_f, label="(f)")
plt.plot(x_list, function_g, label="(g)")

# Set yscale, grid, and legend
plt.yscale('log')
plt.ylim(ymax=100000000)
plt.xscale('log')
plt.xlim(left=1, xmax=1000)

plt.grid()
plt.legend()
plt.savefig("filename.pdf", format='pdf')
plt.show()
