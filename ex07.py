from sympy import Symbol, solve
import numpy as np
import matplotlib.pyplot as plt

x = Symbol('x')

C1 = 2*x + 30
C2 = -x + 90

answer = solve(C1 - C2, x)
quantity = answer[0]
cost = C1.subs({x: quantity})

print('兩模型成本相同時的生產數量 = {}'.format(quantity))
print('兩模型成本相同時的成本 = {} 百元'.format(cost))

x_values = np.linspace(0, 60, 500)
y1 = 2*x_values + 30
y2 = -x_values + 90

plt.plot(x_values, y1, color='blue', label='C1(x) = 2x + 30')
plt.plot(x_values, y2, color='red', label='C2(x) = -x + 90')

plt.plot(
    float(quantity),
    float(cost),
    'go',
    label='Intersection ({}, {})'.format(quantity, cost)
)

plt.xlabel('x')
plt.ylabel('C')
plt.title('Cost Estimation Models')
plt.grid()
plt.legend(loc='best')
plt.show()