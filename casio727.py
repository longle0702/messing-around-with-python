from sympy import symbols, diff, integrate, sin, cos, tan, cot, log, solve, simplify
import cmath
import math

def derivative(f):
    x = symbols('x')
    f_prime = diff(f, x)
    print(f_prime)
    return f_prime

def antiderivative(g):
    x = symbols('x')
    G = integrate(g)
    print(G)
    return G

def integral(f, a, b):
    x = symbols('x')
    G_definite = integrate(f, (x, a, b))
    print(G_definite)
    return G_definite

def log_equation(x):
    x = symbols('x')
    log_equation = log(x + 1, 5) > 2
    return log_equation 


