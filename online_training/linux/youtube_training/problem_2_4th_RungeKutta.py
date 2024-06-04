import numpy as np
from matplotlib import pyplot as plt


def exact_solution(t):
    '''
    Use separation of varioables method to get the exact
    solution.
    '''
    return 12 * (np.exp(t) / (np.exp(t) + 1)**2)


def f(t, x):
    '''
    x_prime = f(t,x)
    '''
    return x * ((1 - np.exp(t)) / (np.exp(t) + 1))


def runge_kutta_4th(M, t, x, h):
    '''
    The 4th-order Runge-Kutta Method (textbook verison).
    Params:
    - M = number of iterations
    - x = inital position
    - t = initial time
    - h = steps
    '''
    error = np.abs(exact_solution(t) - x)
    # print('t =', '%.5f' % t, '; x =', '%.5f' % x, '; error =', error)

    result = []
    for k in range(0, M):
        result.append(x)
        F1 = h * f(t, x)
        F2 = h * f(t + 0.5 * h, x + 0.5 * F1)
        F3 = h * f(t + 0.5 * h, x + 0.5 * F2)
        F4 = h * f(t + h, x + F3)
        x = x + (F1 + 2 * F2 + 2 * F3 + F4) / 6
        t = t + h
        error = np.abs(exact_solution(t) - x)
        print('t =', '%.5f' % t, '; x =', '%.5f' % x, '; error =', error)

    return result


# Set Parameters
h = -0.01
t_points = np.arange(0, -2, h)
x = 3

# Exact Solution
analytic_solution = []
for t in t_points:
    analytic_solution.append(exact_solution(t))

# Via the textbook function
solution = runge_kutta_4th(M=200, t=0, x=3, h=-0.01)

# Error calculation
analytic_solution_array = np.array(analytic_solution)
solution_array = np.array(solution)
error = np.abs(analytic_solution_array - solution_array)

# Plotting params
plt.plot(t_points, analytic_solution, label='exact solution')
plt.plot(t_points, solution, '--', label='numerical solution')
plt.xlabel('t')
plt.ylabel('solution')
plt.legend()
plt.savefig('problem2.pdf')
plt.show()

plt.plot(t_points, error, label='|exact_solution - numerical_solution|')
plt.legend()
plt.xlabel('t')
plt.ylabel('error')
plt.savefig('problem2_error.pdf')
