Collision Resolution by Chaining
--------------------------------
Another option for the project this afternoon, probably the easier one.
Each slot of the hash table holds a linked list
Collisions are handled by adding multiple items to the same linked list
Slot
Index Chain (linked list)
----- -------------------
0     -> None
1     -> ("foo",12)
2     -> ("baz",999)
3     -> None
put("foo", 12)  # hashes to index 1
put("bar", 30)  # hashes to index 2
put("baz", 999) # hashes to index 2 <<
get("beej")     # hashes to index 1
get("baz")
delete("bar")

Put:
Find the hash index
Search the list for the key
If it's there, replace the value
If it's not, append a new record to the list

Get:
Find the hash index
Search the list for the key
If found, return the value
Else return None

Delete:
Find the hash index
Search the list for the key
If found, delete the node from the list, (return the node or value?)
Else return None