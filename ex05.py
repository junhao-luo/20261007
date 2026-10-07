from sympy import Symbol, solve
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')
y = Symbol('y')

eq1 = x + y - 120
eq2 = 3*x + 8*y - 400

answer = solve((eq1, eq2), (x, y))

print('菜鳥業務員須外出天數 = {}'.format(answer[x]))
print('資深業務員須外出天數 = {}'.format(answer[y]))

x_values = np.linspace(0, 120, 500)

y1 = 120 - x_values
y2 = (400 - 3*x_values) / 8

plt.figure(figsize=(10, 6))
plt.plot(x_values, y1, color='blue', label='x + y = 120')
plt.plot(x_values, y2, color='red', label='3x + 8y = 400')

plt.scatter(float(answer[x]), float(answer[y]), color='green', label='(x, y)')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0, 120)
plt.ylim(0, 60)
plt.xticks([0, 20, 40, 60, 80, 100, 120])
plt.yticks([0, 10, 20, 30, 40, 50, 60])
plt.grid(True)
plt.legend(loc='upper right')

plt.show()