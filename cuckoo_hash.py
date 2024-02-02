# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List, Optional

class CuckooHash:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.tables = [[None]*init_size for _ in range(2)]

	def hash_func(self, key: int, table_id: int) -> int:
		key = int(str(key) + str(self.__num_rehashes) + str(table_id))
		rand.seed(key)
		return rand.randint(0, self.table_size-1)

	def get_table_contents(self) -> List[List[Optional[int]]]:
		return self.tables

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.

	def insert(self, key: int) -> bool:
	##################CODE STARTS FROM HERE######################################################################################################
		#initializing the number of displacements, cause we need to track that
		number_of_displacements = 0
		#temporary variable declared to store the current key
		current_key = key

		while number_of_displacements < self.CYCLE_THRESHOLD:
			for id in range(2):
				hash_val = self.hash_func(current_key, id)
				if self.tables[id][hash_val] is None:
					self.tables[id][hash_val] = current_key
					return True
				else:
					current_key, self.tables[id][hash_val] = self.tables[id][hash_val], current_key
					number_of_displacements +=1

		hash_val0 = self.hash_func(current_key,0)
		self.tables[0][hash_val0] = current_key
		return False
	##############################################################################################################################################

	def lookup(self, key: int) -> bool:
	##################CODE STARTS FROM HERE#######################################################################################################
		hash_value0 = self.hash_func(key, 0)
		hash_value1 = self.hash_func(key, 1)

		#Cheking if the key is already present in one of the tables
		if self.tables[0][hash_value0] == key or self.tables[1][hash_value1] == key:
			return True
		return False
	##############################################################################################################################################

	def delete(self, key: int) -> None:
	##################CODE STARTS FROM HERE#######################################################################################################
		hash_val0 = self.hash_func(key, 0)
		hash_val1 = self.hash_func(key, 1)

		if self.tables[0][hash_val0] == key:
			self.tables[0][hash_val0] = None
		elif self.tables[1][hash_val1] == key:
			self.tables[1][hash_val1] = None
	##############################################################################################################################################

	def rehash(self, new_table_size: int) -> None:
	##################CODE STARTS FROM HERE#######################################################################################################
		self.__num_rehashes += 1; self.table_size = new_table_size # do not modify this line

		old_elements = [key for table in self.tables for key in table if key is not None]

		self.tables = [[None for _ in range(new_table_size)] for _ in range(2)]

		failed_keys = []
		for key in old_elements:
			if not self.insert(key):
				failed_keys.append(key)
		
		if failed_keys:
			print(f"Rehashing failed for {len(failed_keys)} keys, attemping with a bigger size")
			self.rehash(new_table_size * 2)

	##############################################################################################################################################
	

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
			
# chash = CuckooHash(10)
# chash.insert(101)
# print(chash.get_table_contents())
# chash.insert(12)
# print(chash.get_table_contents())
# chash.insert(15)
# print(chash.get_table_contents())
