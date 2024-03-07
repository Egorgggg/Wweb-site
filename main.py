def feb(n):
    if n == 1 or n==2:
        return 1    
    else:
        return feb(n-2) + feb(n-1)

print(feb(100))    