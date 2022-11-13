"""
@author: Abhiram Aroop
@since: 19/10/2019
@modified: 24/10/2019
"""

class HashTable: #same as task 3
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
        if table_capacity == None:
            table_capacity = 101
        if hash_base == None:
            hash_base = 31
        self.table = [None] * table_capacity
        self.table_size = table_capacity
        self.base = hash_base
        self.count = 0

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
        pos = self.hash(key)
       
        for i in range(0,self.table_size):
            if self.table[pos] == None:
                raise KeyError
            elif self.table[pos][0] == key:
                return self.table[pos][1]
            else:
                pos = (pos+1)%self.table_size
                
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
        collision = False
        probe = 0
        
        for i in range(0, self.table_size//2):
            
            if self.table[pos] == None:
                self.table[pos] = (key,item)
                self.count += 1
                return
            elif self.table[pos][0] == key:
                self.table[pos] =(key,item)
                return
            else:
                if collision == False:
                    self.collision_count += 1
                    
                pos = (pos+1)%self.table_size
                    
                self.probe_total += 1
                probe += 1
                if probe > self.probe_max:
                    self.probe_max = probe
                collision = True

        self.rehash_count += 1
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
        for prime in Primes:
            if prime > double_size:
                table_size = prime
                break
            
        self.table = [None]*table_size
        self.table_size = table_size
        for i in range(0,old_size):
            self.table[i] = old_table[i]
                

    def statistics(self):
        """
        This function returns number of collusions,probes...etc
        :@param: None
        :@return: (self.collision_count,self.probe_total,self.probe_max,self.rehash_count): integers/float values
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1), constant time
        """
        return (self.collision_count,self.probe_total,self.probe_max,self.rehash_count)

class Freq:
    def __init__(self):
        """
        This function initialises the Frequency class
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: best and worst case: O(1), constant time
        """
        self.max = 0
        self.words = []
        self.count = []
        
    def add_file(self,filename):
        """
        This function adds words in a file into a hashtable
        :@param: filename: Name of a file(string)
        :@return: None
        :@pre-condition: filename must be a string and valid
        :@post-condition: None
        :@complexity: best and worst case: O(n), linear probing
        """
        hash_table = HashTable(100020,123)
        pos = 0

        filename = str(filename)
        file = open(filename,'r',encoding = 'utf-8') 
        read_lines = file.readlines()

        for line in read_lines: #checks every line
            words = line.split(' ')
            words[-1] = words[-1].strip('\n')
                
            for word in words: #checks every word in line
                if word in self.words: #word already found?
                    self.count[self.words.index(word)] += 1
                    hash_table[word] = (word,self.count[self.words.index(word)])
                else: #no,new word
                    self.words.append(word)
                    self.count.append(1)
                    hash_table[word] = (word,1)
            
        
        file.close()
        for i in range(0,len(self.words)):
            if self.count[i] > self.max:
                self.max = self.count[i]
                            
            
    def rarity(self,word):
        """
        This function checks the rarity of a word
        :@param: word: string
        :@return: integer, based on rarity score
        :@pre-condition: word must be a string
        :@post-condition: None
        :@complexity: best and worst case: O(n), n is size of self.words
        """
        no_word = 0
        if word in self.words: #word exist?
            no_word = self.count[self.words.index(word)]
        else: #no, error
            return 3

        if no_word >= self.max/1000:
            if no_word >= self.max/100:
                return 0
            else:
                return 1
        else:
            return 2

    def evaluate_frequency(self,other_filename=None):
        """
        This function finds out the rarity percent of words in a file in relation to another file.
        :@param: other_filename: string 
        :@return: Tuple of 4 floats, based on rarity percent
        :@pre-condition: other_filename must be a string and valid file
        :@post-condition: None
        :@complexity: best and worst case: O(n), n is number of lines in file
        """
        #error catching
        try:
            assert open(other_filename)
        except:
            raise OSError

        words_lst = []
        filename = str(other_filename)
        file = open(filename,'r',encoding = 'utf-8')
        read_lines = file.readlines()

        for line in read_lines: #reads a line
            words = line.split(' ')
            words[-1] = words[-1].strip('\n')
                
            for word in words: #checks a word in line
                if word not in words_lst:
                    words_lst.append(word)

        n_common,n_uncommon,n_rare,n_errors = 0,0,0,0
        
        for i in range(len(words_lst)): #find amounts of each rarity
            if words_lst[i] in self.words:
                if self.rarity(words_lst[i]) == 2:
                    n_rare += 1
                elif self.rarity(words_lst[i]) == 1:
                    n_uncommon += 1
                elif self.rarity(words_lst[i]) == 0:
                    n_common += 1
                
            else:
                n_errors += 1

        #conver to percentages
        common = ((n_common)/( n_common+n_uncommon+n_rare+n_errors))*100
        uncommon = ((n_uncommon)/( n_common+n_uncommon+n_rare+n_errors))*100
        rare = ((n_rare)/( n_common+n_uncommon+n_rare+n_errors))*100
        errors = ((n_errors)/( n_common+n_uncommon+n_rare+n_errors))*100
        
        return (common,uncommon,rare,errors)
                
#Comparing 98,1342, 2600 files with 84(evaluate_frequency)
#Remove doc-strings to test
"""
freq = Freq()
freq.add_file('98-0.txt')
print(freq.evaluate_frequency('84-0.txt'))
freq = Freq()
freq.add_file('1342-0.txt')
print(freq.evaluate_frequency('84-0.txt'))
freq = Freq()
freq.add_file('2600-0.txt')
print(freq.evaluate_frequency('84-0.txt'))
"""
