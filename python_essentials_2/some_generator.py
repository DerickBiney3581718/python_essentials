def some_generator(n):
    for i in range(n):
        yield i  #gen obj

for i in some_generator(5):
    print(i)
 
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for v in powers_of_2(8):
    print(v)

t = list(powers_of_2(8))
print('t values: ', t)