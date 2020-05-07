# Slow calculation caching
​
cache = {}
​
def fib(n):
    if n <= 1:
        return n
​
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
​
    return cache[n]
​
for i in range(10000):
    print(fib(i))

# Lookup Table

import math
​
cache = {}
​
def build_lookup_table():
    for i in range(1, 1000):
        inv_square_root(i)
​
def inv_square_root(n):
    if n not in cache:
        cache[n] = 1 / math.sqrt(n)
​
    return cache[n]
​
for i in range(1, 6):
    print(inv_square_root(i))
​
# Sorting

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}
​
## Sorting by Key:
​
items = list(d.items())
​
print(items)
​
items.sort()
​
print(items)
​
for i in items:
    print(f'{i[0]}: {i[1]}')
​
## Sort by Value:
​
items = list(d.items())
​
print(items)
​
"""
def get_key(e):
    return e[1]
​
items.sort(key=get_key)
"""
items.sort(key=lambda e: e[1], reverse=True)
​
print(items)
​
for i in items:
    print(f'{i[0]}: {i[1]}')

# Create Decode Table

encode_table = {
    'A': 'H', 'B': 'Z', 'C': 'Y', 'D': 'W', 'E': 'O', 'F': 'R', 'G': 'J',
    'H': 'D', 'I': 'P', 'J': 'T', 'K': 'I', 'L': 'G', 'M': 'L', 'N': 'C',
    'O': 'E', 'P': 'X', 'Q': 'K', 'R': 'U', 'S': 'N', 'T': 'F', 'U': 'A',
    'V': 'M', 'W': 'B', 'X': 'Q', 'Y': 'V', 'Z': 'S'
}
​
decode_table = {}
​
for k, v in encode_table.items():
    decode_table[v] = k
​
def encode(s):
    r = ""
​
    for c in s:
        r += encode_table[c]
​
    return r
​
def decode(s):
    r = ""
​
    for c in s:
        r += decode_table[c]
​
    return r
​
print(encode("ATTACKATDAWN"))
​
print(decode("HZYW"))

# Letter Count

def letter_count(s):
    d = {}
​
    for c in s:
        if c.isspace():
            continue
​
        c = c.lower()
​
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
​
    return d
​
def print_sorted_letter_count(s):
    c = letter_count(s)
​
    items = list(c.items())
​
    items.sort(key=lambda e: e[1], reverse=True)
​
    for i in items:
        print(f'{i[0]}: {i[1]}')
​
​
​
print_sorted_letter_count("aaabbc")
#print_sorted_letter_count("Hello!")
#print_sorted_letter_count("The quick brown fox jumps over the lazy dogs")


# Indexing

records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]
​
​
def build_index(rec):
    idx = {}
​
    for r in rec:
        name, dept = r
​
        if dept not in idx:
            idx[dept] = []
​
        idx[dept].append(name)
​
    return idx
​
​
idx = build_index(records)
​
## print all the departments
for i in idx:
    print(i)
​
## print everyone in Engineering:
print(idx["Engineering"])
