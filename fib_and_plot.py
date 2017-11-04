#!/usr/bin/python
''' Calculate and plot the Fibonacci numbers '''

from matplotlib.pyplot import draw, figure, plot, show, scatter

show(block=False)


def fib(n):
    ''' Calculate a list of Fibonacci numbers up to n '''

    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return(result)


n = input("Enter an integer: ")
print("\nHere are the Fibonacci numbers up to " + str(n) + "\n")
print fib(n+1)
print("\n")

y = fib(n + 1)
x = range(1, len(y) + 1)
scatter(x, y)
draw()
show()
