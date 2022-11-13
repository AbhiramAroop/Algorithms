"""
@author: Abhiram Aroop
@since: 13/10/2019
@modified: 17/10/2019
"""

import task1
import timeit
import csv

def load_dictionary(hash_table,filename,time_limit=None):
    """
    This function loads words in a file into a hash table
    :@param: hash_table: a hash_table 
    :@param: filename: str, name of the file to be read
    :@param: time_limit: a number/None value
    :@return: None
    :@pre-condition: hash_table, must be the one from task1
    :@post-condition: None
    :@complexity: best and worst case: O(n), where n is the size of table
    """
    #READ FILE
    filename = str(filename)
    file = open(filename,"r")
    read_lines = file.readlines()

    #START TIMER
    start = timeit.default_timer()
    for line in read_lines: #Check all lines
        if time_limit != None: #max time?
            if timeit.default_timer() - start > time_limit:
                raise Exception("Time Out!")

        line.strip('\n') #Get rid of \n to save space
        hash_table[line] = (line,1)
            

def load_dictionary_time(hash_base,table_size,filename,max_time):
    """
    This function computes the number of words and time taken to insert words from filename into a hashtable
    :@param: hash_base: an integer, hash table base value
    :@param: table_size: an integer, size of hash table
    :@param: filename: string, name of file
    :@param: max_time: a number>0/None value 
    :@return: (words,time): number of words and time taken to store words in hash table
    :@pre-condition: hash_base and table_size must be integers
    :@post-condition: None
    :@complexity: best and worst case: O(n), where n is the size of table
    """
    hash_table = task1.HashTable(table_size,hash_base)

    words = 0
    #READ FILE
    filename = str(filename)
    file = open(filename,"r",encoding = 'utf-8') #open file and read
    read_lines = file.readlines()
    start = timeit.default_timer() #start timer
    
    for line in read_lines: #CHECK EACH LINE
        if max_time != None:
            if timeit.default_timer() - start > max_time: #Out of time?
                time = None
                break
        
        line.strip('\n') #remove \n to save space
        hash_table.__setitem__(line,1)
        words += 1
        time = timeit.default_timer()-start #final time
    
    return (words,time)


def table_load_dictionary_time(max_time):
    """
    This function computes the number of words and time taken to insert words from filename into a hashtable then stores into a csv file
    :@param: max_time: a number/None value
    :@return: None: number of words and time taken to store words in hash table
    :@pre-condition: max_time must be number > 0
    :@post-condition: None
    :@complexity: best and worst case: O(n), where n is the size of table
    """
    graph = [[1,250727],
             [27183,402221],
             [250726,1000081]]
    
    files = ['english_small.txt',
             'english_large.txt',
             'french.txt']

    data = []

    #Nested loop to compute collect all 9 data set
    for i in range(0,len(files)):
        for j in range(0,len(graph)):
            data.append([])
            data[len(data)-1].append(graph[j][0])
            data[len(data)-1].append(graph[j][1])
            data[len(data)-1].append(files[i])
            (w,t) = load_dictionary_time(graph[j][0],graph[j][1],files[i],max_time)
            if t == None:
                t = 'TIMEOUT'
            data[len(data)-1].append(w)
            data[len(data)-1].append(t)
            
    with open('output_task2.csv','w',encoding='utf-8') as csvFile: #stores the computational times as a list and adds it to a csv file
        writer = csv.writer(csvFile)
        writer.writerows(data) #write the in data as rows of the csv files
    csvFile.close()

#table_load_dictionary_time(120)
    

   
