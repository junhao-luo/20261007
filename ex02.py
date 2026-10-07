from sympy import Symbol
from sympy.plotting import plot

x = Symbol('x')

lines = plot(5*x - 10, 2*x + 6, (x, -10, 10), title='Sympy', xlabel='x', ylabel='f(x)', legend=True, show=False)

lines[0].line_color = 'cyan'
lines[0].label = '5x - 10'

lines[1].line_color = 'green'
lines[1].label = '2x + 6'

lines.show()