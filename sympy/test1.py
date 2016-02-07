# coding=utf-8
############################################################
# Простые примеры на sympy
############################################################
from sympy.solvers import solve
from sympy import sin, limit
from sympy import *

x = Symbol('x')
a = Symbol('a')

print "Solve: x**3 + 2*x**2 + 4*x + 8 = 0"
res = solve(Eq(x**3 + 2*x**2 + 4*x + 8, 0), x)
print res
print ""

print "Simplify: a = 1/x + (x*sin(x) - 1)/x"
eq = Eq(a, 1/x + (x*sin(x) - 1)/x)
print simplify(eq)
print ""

print "Limit: (sin(x)-x)/x**3"
res = limit((sin(x)-x)/x**3, x, 0)
print res
print ""

print "Solve: df/dt = 1 - 9*f"
f = Function('f')
res = dsolve(Eq(Derivative(f(x),x,x), 1 - 9*f(x)), f(x))
print res