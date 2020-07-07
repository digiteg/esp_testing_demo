# --------------------------------------------------------------------------------------------
# Fibonacci example
#
# Lets try to apply few testing techniques which we learned on fibonacci function example
# - Boundary Values
# - Error Guessing

# returns fibonacci number
def fib(n):
# To fix Error Guessing tests uncomment this lines
    if n is None or type(n) is str or n < 0:
        return 0
    
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)