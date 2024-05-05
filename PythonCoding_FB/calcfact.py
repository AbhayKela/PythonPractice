n = int(input("Provide number for the factorial? "))

factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

print(factorial(n))