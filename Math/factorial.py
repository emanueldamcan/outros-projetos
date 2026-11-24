num = float(input("Type the number: "))
def factorial_function(n):
    if n <= 1:
        return 1
    return n * factorial_function(n-1)
print(factorial_function(num))