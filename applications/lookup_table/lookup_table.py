import math
import random

cache = {}

##Builds the Look Up Library using the x and y ranges I know will be used based on below 'test'
def look_up():
    for x in range(2, 14):
        for y in range(3, 6):
            slowfun(x, y)

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    if (x, y) not in cache:##stores each calculated above in cache
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[(x, y)] = v
    return cache[(x, y)]## if (x, y) already a key in cache returns the 'answer' or value from cache/dictionary/hashtable

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
