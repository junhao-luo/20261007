from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')

eq1 = x + y - 30
eq2 = 4*x + 7*y - 150

answer = solve((eq1, eq2), (x, y))

is_valid = answer[x] % 1 == 0 and answer[y] % 1 == 0 and answer[x] >= 0 and answer[y] >= 0 and answer[x] + answer[y] == 30 and 4*answer[x] + 7*answer[y] >= 150 and answer[y] <= answer[x] / 2

if is_valid:
    print(answer)
    print('甲外出天數 = {}'.format(answer[x]))
    print('乙外出天數 = {}'.format(answer[y]))
    print('符合乙不超過甲一半：{}'.format(is_valid))
else:
    print('符合乙不超過甲一半：{}'.format(is_valid))