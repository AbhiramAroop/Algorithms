"""
@author: Abhiram Aroop
@since: 19/10/2019
@modified: 24/10/2019
"""

import task2
import csv
import timeit
class BinaryTreeNode:
    def __init__(self, key=None, value=None, left=None, right=None):
        """
        This function initilises node for BST
        :@param: key,value,left,right: None, value is integer the rest are strings
        :@return: None
        :@pre-condition: value must be integer, the rest must be strings
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        self.key = key
        self.item = value
        self.left = left
        self.right = right

    def __str__(self):
        """
        This function returns a tuple of (key,item)
        :@param: None
        :@return: tuple of key and item
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        return " (" + str(self.key) +  ", " + str(self.item) + " ) "


class BinarySearchTree:
    def __init__(self):
        """
        This function initilises a root for BST
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        self.root = None

    def is_empty(self):
        """
        This function checks whether a root is empty
        :@param: None
        :@return: Boolean, True or False
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        return self.root is None

    def __len__(self):
        """
        This function finds the length of the BST
        :@param: None
        :@return: integer
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        return self._len_aux(self.root)

    def _len_aux(self,current):
        """
        This function finds length of a root in BST
        :@param: None
        :@return: Integer
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        if current is None:
            return 0
        else:
            return 1+self._len_aux(current.left)+self._len_aux(current.right)

    def inorder(self,f):
        """
        This function checks whether tree is in correct order
        :@param: f
        :@return: Boolean, True or False
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        return self._inorder_aux(self.root,f)

    def _inorder_aux(self,current,f):
        """
        This function checks whether tree is in correct order
        :@param: current, f
        :@return: Boolean, True or False
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        if current is not None:
            self._inorder_aux(current.left, f)
            f(current)
            self._inorder_aux(current.right, f)

    def __contains__(self, key):
        """
        This function checks whether BST contains a certain key
        :@param: key, string
        :@return: Boolean, True or False
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        #return self._contains_aux(key, self.root)
        return self._contains_iter(key)

    def _contains_aux(self, key, current_node):
        """
        This function checks whether current node contains the given key
        :@param: key, string
        :@param: current_node, integer
        :@return: Boolean, True or False
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        if current_node is None:  # base case
            return False
        elif key == current_node.key:
                return True
        elif key < current_node.key:
            return self._contains_aux(key, current_node.left)
        elif key > current_node.key:
            return self._contains_aux(key, current_node.right)

    def _contains_iter(self, key):
        """
        This function checks whether current node contains the given key
        :@param: key, string
        :@return: Boolean, True or False
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        current_node = self.root
        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True
        return False

    def __getitem__(self, key):
        """
        This function returns an item based on key
        :@param: key, string
        :@return: self._get_item_iter(key, self.root): integer
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        return self._get_item_iter(key, self.root)

    def _get_item_aux(self, key, current_node):
        """
        This function gives item for a given key and node
        :@param: key, string
        :@param: current_node, integer
        :@return: string
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        if current_node is None:  # base case
            raise KeyError("Key not found")
        elif key == current_node.key:
                return current_node.item
        elif key < current_node.key:
            return self._get_item_aux(key, current_node.left)
        elif key > current_node.key:
            return self._get_item_aux(key, current_node.right)

    def _get_item_iter(self, key, current_node):
        """
        This function gives item for a given key and node
        :@param: key, string
        :@param: current_node, integer
        :@return: string
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        while current_node is not None:
          if key < current_node.key:
            current_node = current_node.left
          elif key > current_node.key:
            current_node = current_node.right
          else:
            assert current_node.key == key
            return current_node.item
        raise KeyError("Key not found")

    def __setitem__(self, key, value):
        """
        This function sets a key and value based on key
        :@param: key, string
        :@param: value, integer
        :@return: none
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        self._insert_iter(key, value)

    def _insert_aux(self, key, value, current_node):
        """
        This function inserts a key and value based on key, on the current node
        :@param: key, string
        :@param: value, integer
        :@param: current_node: integer
        :@return: current_node: 
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        if current_node is None:
            current_node = BinaryTreeNode(key, value)
        elif key < current_node.key:
            current_node.left =  self._insert_aux(key, value, current_node.left)
        elif key > current_node.key:
            current_node.right = self._insert_aux(key, value, current_node.right)
        elif key == current_node.key:
            current_node.item = value
        return current_node

    def _insert_iter(self, key, value):
        """
        This function inserts a key and value based on key
        :@param: key, string
        :@param: value, integer
        :@return: none
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1)
        """
        if self.root is None:
            self.root = BinaryTreeNode(key, value)
            return

        current_node = self.root
        while True:
          if key < current_node.key:
            if current_node.left is None:
              current_node.left = BinaryTreeNode(key, value)
              break
            else:
              current_node = current_node.left
          elif key > current_node.key:
            if current_node.right is None:
              current_node.right = BinaryTreeNode(key, value)
              break
            else:
              current_node = current_node.right
          else:
            assert current_node.key == key
            current_node.item = item
            break


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
        #default values
        if table_capacity == None:
            table_capacity = 101
        if hash_base == None:
            hash_base = 31
        self.table = [None] * table_capacity #create table
        self.table_size = table_capacity
        self.base = hash_base
        self.count = 0
        self.current = 0
        self.collision = False
        self.previous = 0

        self.collision_count = 0
        self.probe_total = 0
        self.probe_max = 0
        self.rehash_count = 0
  
    def __getitem__(self, key=None):
        """
        This function gets item at a given key of the hash table
        :@param: key: a string less than  or equal to length 10
        :@return: self.table[pos][1]: value at given key
        :@pre-condition: key must be string
        :@post-condition: None
        :@complexity: best and worst case: O(n), where n is self.table_size
        """
        if key == None: #no key?
            raise KeyError
        pos = self.hash(key) 
        if pos > self.table_size: #position is bigger than what table can fit?
            raise KeyError

        tree = self.table[pos]
        if tree == None: #nothing in tree
            raise KeyError
        if tree.__contains__(key) == False: #Tree does not contain key?
            return KeyError
        
        item = tree.__getitem__(key)
        return item
        
    
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
        while pos > self.table_size: #out of index?
            self.rehash_count += 1
            self.rehash() #increase table size
            
        if self.table[pos] == None: #Nothing in position
            #initilise tree
            my_tree = BinarySearchTree()
            my_tree.__setitem__(key,item)
            self.table[pos] = my_tree
            self.collision = False
            self.current = 0
        else: #tree in position
            self.table[pos].__setitem__(key,item)
            self.current += 1
            
        self.collision_count = self.table[pos].__len__()-1      
        self.count += 1
        if self.current > self.probe_max: #update max
            self.probe_max = self.current
        
                

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
        table_size = double_size
        old_table = self.table
        old_size = self.table_size
        for prime in Primes: #choose best prime form list
            if prime > double_size:
                table_size = prime
                break
            
        self.table = [None]*table_size
        self.table_size = table_size
        for i in range(0,old_size):
            self.table[i] = old_table[i]
                
    def total_probe(self,i):
        """
        This function is used to compute the total probe chain using recursion
        :@param: i, an integer >= 0
        :@return: 0, (i-1)+self.total_probe(i-1): an integer based on computed result
        :@pre-condition: i must be integer>0
        :@post-condition: None
        :@complexity: best and worst case: O(log(n)): recusive function
        """
        if i == 1 or i == 0:
            return 0
        else:
            return (i-1)+self.total_probe(i-1)
        
        
    def statistics(self):
        """
        This function returns number of collusions,probes...etc
        :@param: None
        :@return: (self.collision_count,self.probe_total,self.probe_max,self.rehash_count): integers/float values
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1), constant time
        """

        for i in range(0,self.table_size): #finds total probe amount
            if self.table[i] != None and self.table[i].__len__() > 1:
                self.probe_total += self.total_probe(self.table[i].__len__())

        
        return (self.collision_count,self.probe_total,self.probe_max,self.rehash_count)


def load_dictionary_statistics(hash_base,table_size,filename,max_time):
    """
    This function returns number of collusions,probes...etc
    :@param: hash_base: an integer, base of hash table
    :@param: table_size: an integer, size of hash table
    :@param: filename: string, name of file to be read
    :@param: max_time: float/integer >0/None, max time which cannot be exceeded
    :@return: (words,time,self.collision_count,self.probe_total,self.probe_max,self.rehash_count): integers/float values
    :@pre-condition: None
    :@post-condition: None
    :@complexity: best and worst case: O(n), n is number of lines in file
    """
    hash_table= HashTable(table_size,hash_base)

    words = 0
    #READ FILE
    filename = str(filename)
    file = open(filename,"r",encoding = 'utf-8')
    read_lines = file.readlines()
    start = timeit.default_timer()
    
    for line in read_lines: #CHECK EACH LINE
        if max_time != None:
            if timeit.default_timer() - start > max_time: #Out of time?
                time = None
                break
        
        line.strip('\n')
        hash_table[line] = (line,1)
        words += 1
        time = timeit.default_timer()-start
        
    return (words,time,hash_table.statistics()[0],hash_table.statistics()[1],hash_table.statistics()[2],hash_table.statistics()[3])
    
def table_load_dictionary_statistics(max_time):
    """
    This function transvers all data from load_dictionary_statistics function into a csv file for different cases
    :@param: max_time: float/integer >0/None, max time which cannot be exceeded
    :@return: None
    :@pre-condition: None
    :@post-condition: None
    :@complexity: best and worst case: O(n),where n is size of table
    """
    graph = [[1,250727],
             [27183,402221],
             [250726,1000081]]
    
    files = ['english_small.txt',
             'english_large.txt',
             'french.txt']
    

    data = []

    #iterates and computes data for all 9 conditions
    for i in range(0,len(files)):
        for j in range(0,len(graph)):
            data.append([])
            data[-1].append(graph[j][0])
            data[-1].append(graph[j][1])
            data[-1].append(files[i])
            (w,t,c,pt,pm,rc) = load_dictionary_statistics(graph[j][0],graph[j][1],files[i],max_time)
            if t == None:
                t = max_time+10
            data[-1].append(w)
            data[-1].append(t)
            data[-1].append(c)
            data[-1].append(pt)
            data[-1].append(pm)
            data[-1].append(rc)
            
    with open('output_task5.csv','w',encoding = 'utf-8') as csvFile: #stores the computational times as a list and adds it to a csv file
        writer = csv.writer(csvFile)
        writer.writerows(data) #write the in data as rows of the csv files
    csvFile.close()


#table_load_dictionary_statistics(120)

