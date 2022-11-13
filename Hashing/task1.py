"""
@author: Abhiram Aroop
@since: 13/10/2019
@modified: 17/10/2019
"""


class HashTable:
    def __init__(self, table_capacity=None, hash_base=None):
        """
        This function creates a hash table, represented as a list
        :@param: table_capacity: an integer or None value
        :@param: hash_base: an integer or None value
        :@return: None
        :@pre-condition: table_capacity and hash_base must be integers or None
        :@post-condition: None
        :@complexity: best and worst case: O(n), where n is value of table_capacity
        """
        #Initial conditions
        if table_capacity == None:
            table_capacity = 101
        if hash_base == None:
            hash_base = 31
        #create table
        self.table = [None] * table_capacity
        self.table_size = table_capacity
        self.base = hash_base
        self.count = 0
  
    def __getitem__(self, key=None):
        """
        This function gets item at a given key of the hash table
        :@param: key: a string less than  or equal to length 10
        :@return: self.table[pos][1]: value at given key
        :@pre-condition: key must be string
        :@post-condition: None
        :@complexity: best and worst case: O(n), where n is self.table_size
        """
        pos = self.hash(key)

        #iteration
        for i in range(0,self.table_size): 
            if self.table[pos] == None: #Nothing in key value
                raise KeyError
            elif self.table[pos][0] == key: #key is there
                return self.table[pos][1]
            else:
                pos = (pos+1)%self.table_size #check next position
                
        raise KeyError(key)
    
    def __setitem__(self, key, item):
        """
        This function sets item at a given key of the hash table
        :@param: key: a string less than  or equal to length 10
        :@param: item: an integer
        :@return: None
        :@pre-condition: key must be string, item must be an integer
        :@post-condition: None
        :@complexity: best and worst case: O(n), where n is self.table_size
        """
        pos = self.hash(key)
        
        for i in range(0, self.table_size):
            if self.table[pos] == None: #Nothing in position
                self.table[pos] = (key,item)
                self.count += 1
                return
            elif self.table[pos][0] == key: #key exists
                self.table[pos] =(key,item)
                return
            else:
                pos = (pos+1)%self.table_size #next position if collision

        self.rehash()
        self.__setitem__(key,item)

    def __contains__(self, key):
        """
        This function states whether there is a value of given key in hash table
        :@param: key: a string less than  or equal to length 10
        :@return: Boolean: true if there is key in table or false if not
        :@pre-condition: key must be string
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        if self.table[self.hash(key)] != None:
            return True
        else:
            return False
        
    def hash(self, key):
        """
        This function computes the hash value for a given key
        :@param: key: a string less than  or equal to length 10
        :@return: value: an integer 
        :@pre-condition: key must be string
        :@post-condition: None
        :@complexity: best and worst case: O(n),where n is length of key
        """
        #Formula from lectures
        if key != "":
            value = 0
            for i in range(0,len(key)):
                value = (value*self.base + ord(key[i])) % len(self.table)
        else:
            value = 0
        
        return value
        

    def rehash(self):
        """
        This function computes the hash value for a given key
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(n),where n is size of table
        """
        Primes = [ 3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761,
                   919, 1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591,
                   17519, 21023, 25229, 30313, 36353, 43627, 52361, 62851, 75521, 90523, 108631, 130363, 156437,
                   187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263,
                   1674319, 2009191, 2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369]
        double_size = self.table_size * 2
        old_table = self.table
        old_size = self.table_size
        table_size = self.table_size
        
        for prime in Primes: #all prime values in list
            if prime > double_size: #match condition?
                table_size = prime
                break
        if Primes[-1] < double_size: #no prime??
            raise ValueError
        self.table = [None]*table_size
        self.table_size = table_size
        for i in range(0,old_size):
            self.table[i] = old_table[i]


