
"""
Linked Lists Refresher
----------------------
​
(1)->(2)->(3)->None
 ^
head
​
None
 ^
head
"""
​
"""
class HashTableEntry:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
"""
​
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
​
​
head = None  # Empty linked list
​
# Insert (at head)
# Append (at tail)
# Find
# Delete
​
def insert_at_head(value):
	global head
​
	n = Node(value)
	n.next = head
	head = n
​
	return n
​
def find(value):
	global head
​
	cur = head
​
	while cur is not None:
		if cur.value == value:
			return cur
​
		cur = cur.next
​
	return None
​
def append_at_tail(value):
	global head
​
	n = Node(value)
​
	if head is None:
		head = n
		return
​
	cur = head
​
	while cur.next is not None:
		cur = cur.next
​
	cur.next = n
​
def delete(value):
	global head
​
	# Find the node to delete
	cur = head
​
	# Delete the head special case
	if cur.value == value:
		head = head.next
		cur.next = None
		return cur
​
	prev = None
​
	while cur is not None:
		if cur.value == value:
			# Found it, delete it
			prev.next = cur.next
			cur.next = None
			return cur
​
		prev = cur
		#prev = prev.next
		cur = cur.next
​
	return None