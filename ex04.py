from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')

eq1 = x + y - 120
eq2 = 3*x + 8*y - 400

answer = solve((eq1, eq2), (x, y))

print('菜鳥業務員須外出天數 = {}'.format(answer[x]))
print('資深業務員須外出天數 = {}'.format(answer[y]))