def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    
index = 6
print(fibonacci(index))

fibonacci_runtime = "2^N"
