def fib(n):
    fibn1= fibn2 = 1
    for i in range(n):
        yield fibn2
        if i > 0:
            fibn1, fibn2 = fibn2,  fibn1 + fibn2
fibs = list(fib(8))
print(fibs)

n = 7
for v in ( x if x % 2 else 0 for x in range(n)): #? yield can be only used in functions alors then use of parentheses
    print(v)
    
#* map, filter , args: func, list
#! both return generators