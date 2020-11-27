class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None

class linked_list:
	def __init__(self):
		self.head=node()

	# Adds new node containing 'data' to the end of the linked list.
	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	# Returns the length (integer) of the linked list.
	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total

	# Prints out the linked list in traditional Python list format.
	def display(self):
		elems=[]
		cur_node=self.head
		while cur_node.next!=None:#while the pointer of the current nodes next field is not equal to null
			cur_node=cur_node.next #set the current node equal to the next node
			elems.append(cur_node.data)#append the data our current node to our List
		print(elems)#print the elements

	# Returns the value of the node at 'index'.
	def get(self,index):#extractor function to pull out a data point at a certain index from the linked list
		if index>=self.length() or index<0: # added 'index<0' post-video.#check to make sure the index is not out of the range of the linked list
			print("ERROR: 'Get' Index out of range!")#prints error message
			return None
		cur_idx=0 #contains the value of the current index we are looking at
		cur_node=self.head#contains the current node we are looking at which starts with the head node
		while True:
			cur_node=cur_node.next#incrementing the current node by setting it to the next node
			if cur_idx==index: return cur_node.data#checking whether the current index is the same as the one provided by the user then we know we are at the data point to be extracted
			cur_idx+=1#otherwise increment the current index

	# Deletes the node at index 'index'.
	def erase(self,index):
		if index>=self.length() or index<0: # added 'index<0' post-video#check to make sure the index is not out of the range of the linked list
			print("ERROR: 'Erase' Index out of range!")
			return
		cur_idx=0#contains the value of the current index we are looking at
		cur_node=self.head#contains the current node we are looking at which starts with the head node
		while True:
			last_node=cur_node#setting the current nodes as the last node.
			cur_node=cur_node.next#incrementing the current node by setting it to the next node
			if cur_idx==index:#check to find if we are at the index the user provided
				last_node.next=cur_node.next#change the pointer for the last node to be the one skipped past the current node
				return
			cur_idx+=1

	# Allows for bracket operator syntax (i.e. a[0] to return first item).
	def __getitem__(self,index):
		return self.get(index)


	#######################################################
	# Functions added after video tutorial

	# Inserts a new node at index 'index' containing data 'data'.
	# Indices begin at 0. If the provided index is greater than or
	# equal to the length of the linked list the 'data' will be appended.
	def insert(self,index,data):
		if index>=self.length() or index<0:
			return self.append(data)
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index:
				new_node=node(data)
				prior_node.next=new_node
				new_node.next=cur_node
				return
			prior_node=cur_node
			cur_idx+=1

	# Inserts the node 'node' at index 'index'. Indices begin at 0.
	# If the 'index' is greater than or equal to the length of the linked
	# list the 'node' will be appended.
	def insert_node(self,index,node):
		if index<0:
			print("ERROR: 'Erase' Index cannot be negative!")
			return
		if index>=self.length(): # append the node
			cur_node=self.head
			while cur_node.next!=None:
				cur_node=cur_node.next
			cur_node.next=node
			return
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index:
				prior_node.next=node
				return
			prior_node=cur_node
			cur_idx+=1

	# Sets the data at index 'index' equal to 'data'.
	# Indices begin at 0. If the 'index' is greater than or equal
	# to the length of the linked list a warning will be printed
	# to the user.
	def set(self,index,data):
		if index>=self.length() or index<0:
			print("ERROR: 'Set' Index out of range!")
			return
		cur_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index:
				cur_node.data=data
				return
			cur_idx+=1

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print("element at 2nd index: %d" % my_list.get(2))
print("element erased at 2nd index is: " + str(my_list.erase(1)))
my_list.display()
