import task2
import csv
import timeit

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
        
        for i in range(0, self.table_size):
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
    file = open(filename,"r",encoding = 'utf-8') #open and read file
    read_lines = file.readlines()
    start = timeit.default_timer() #start time
    
    for line in read_lines: #CHECK EACH LINE
        if max_time != None:
            if timeit.default_timer() - start > max_time: #Out of time?
                time = None
                break
        
        line.strip('\n')
        hash_table[line] = (line,1)
        words += 1
        time = timeit.default_timer()-start #finish time
        
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
    
    #files2 = ['words_simple.txt'] #SKIP

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
            
    print(data)
    with open('output_task3.csv','w',encoding='utf-8') as csvFile: #stores the computational times as a list and adds it to a csv file
        writer = csv.writer(csvFile)
        writer.writerows(data) #write the in data as rows of the csv files
    csvFile.close()


#table_load_dictionary_statistics(120)


