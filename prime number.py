lst = (i for i in range(1,11))
plusone = lambda i:i+1
lst = list(map(plusone,lst))
print(lst)
