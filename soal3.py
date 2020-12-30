fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)
n = 8
result = ""
for index in range(n):
    result += str(fib(index)) + " "
print(result)