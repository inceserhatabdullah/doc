lst = [1,2,3,4,5,6,7,8,9,10]

def f(x):
    print(f'x: {x} --> x ** x: {x ** x}')
    return x ** x
def _f(x):
    if x % 2 == 0:
       f(x)
        
list(map(f, lst))
print()
list(filter(_f, lst))