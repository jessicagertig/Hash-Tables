"""
[ "Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit" ]
   0        1        2        3      4       5              6             7
​
"beej"
"elit"
​
f("elit") -> 7
f("ipsum") -> 1
f("ipsum") -> 1
f("foobar") -> 1
​
1. Get bytes for the key
2. Make up a function that returns an index for those bytes
   * Adding the bytes
   * Modding with the hash table size
"""
​
# How many slots the hash table has
hash_table_size = 8
​
# Space to hold values
hash_table = [None] * hash_table_size
​
def myhash(s):
	"""
	Naive hashing function to turn a string into a number.
​
	Don't use this in real life, ever. It's a horrible hashing function.
​
	* It doesn't give a nice uniform distribution over the space
	* Collisions are far more common than they need to be
​
	Output is 32 bits.
	"""
​
	# Convert the argument to a string, and then to the bytes of that
	# string:
	str_bytes = str(s).encode()
​
	total = 0
​
	# Loop through all the bytes
	for b in str_bytes:
		total += b
​
		total &= 0xffffffff  # clamp to 32 bits
​
		# To make your DJB2 hash correct, add this as the last line of the loop:
		#total &= 0xffffffff  # 32-bit (8 f's)
​
		# To make your FNV-1 hash correct, add this as the last line of the loop:
		#total &= 0xffffffffffffffff  # 64-bit (16 f's)
​
	return total
​
def hash_index(s):
	"""
	Take a hash value and make sure it's in the range of the size
	of the hash table (so it won't fall out of bounds).
	"""
	h = myhash(s)
​
	return h % hash_table_size
​
def put(key, value):
	"""
	Store a value in the table by a key.
	"""
	# Get the index into the hash table list
	index = hash_index(key)
	hash_table[index] = value
​
def get(key):
	"""
	Get a value from the table by a key.
	"""
	index = hash_index(key)
	return hash_table[index]
​
def delete(key):
	"""
	Delete a value in the table by a key.
	"""
	index = hash_index(key)
	hash_table[index] = None
​
if __name__ == "__main__":
	# If running from the command line
	print(hash_index("Hello"))  # 4
	print(hash_index("foobar"))  # 1
	print(hash_index("cats"))
	print(hash_index("beej"))
	print(hash_index("foobaz"))  # 1, collision
	print(hash_index("qux"))
​
	put("Hello", 37)   # similar to dict: d["Hello"] = 37
	put("foobar", 128)
	put("cats", "dogs")
​
	print(hash_table)
​
	print(get("Hello"))  # 37
​
	print(get("Hello"))
	print(get("beej"))
	print(get("foobar"))
​
	delete("Hello")
	print(get("Hello"))  # Non