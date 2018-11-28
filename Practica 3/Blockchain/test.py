import time
from timeit import Timer

def my_timeit(func, *args, **kwargs):
    output_container = []
    def wrapper():
        output_container.append(func(*args, **kwargs))
    timer = Timer(wrapper)
    delta = timer.timeit(1)
    return delta, output_container.pop()

def f():
    x = 52352346523622353245234543652362362345235324523532534262234252352345235325325235325235342535**3435%25452353326326246234624525235
    print("Ejecutando f")
    return 4
def g():
    print("Ejecutando g")
def h():
    print("Ejecutando h")

# print(timeit.timeit('[func(1) for func in (f,g,h)]', globals=globals()))
#print(timeit.timeit("f()", globals=globals(), number=1))
# t = timeit.Timer(f)
# print(t.timeit(number=1))


delta, result = my_timeit(f)
print(delta)
print(result)
