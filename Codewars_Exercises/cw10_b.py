def find(n):
    # Code heredef find(n):
    return sum(i for i in range(1, n+1) if i % 3 == 0 or i % 5 == 0)