import random
import timeit
import math

def counting_sort(a_list,b,place):
    """
    This function implements counting sort for a certain place value of a given list of positive integers with a certain base.

    @param: a_list: A list of positive integers, b: the base for sorting, place: An integer used to determine the place value of sorting
    @return: a_list: the sorted (only for a certain place value) version of the input list
    @pre-condition: a_list must only contain positive integers, b must be integer greater than 2 and place must be non-negative integer.
    @complexity: best and worst case: O(N + b), where N is total number of integers in input list and b is the base
    """
    sorting_list = [0] * len(a_list) #An additional list to perform sorting actions on
    count_arr = [0] * (b) #the length of count array is as big as the base.

    for i in range(0,len(a_list)):
        index = (a_list[i] // b ** place) % b #Index to increment counting sort and ensures that it only takes value from correct place value
        count_arr[index] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1] #adding previous element to current element(ignoring 1st element)

    for i in range(len(a_list)-1,-1,-1):
        index = (a_list[i] // b ** place) % b 
        count_arr[index] -= 1 #in order to have new index for the same number
        sorting_list[count_arr[index]] = a_list[i] 

    a_list = sorting_list[:] 
    return a_list


def radix_sort(num_list,b):
    """
    This function implements radix sort to a given list of positive integers with a certain base.
    This is done without modifying the orginal list.

    @param: num_list: A list of positive integers, b: the base for sorting
    @return: sorted_list: a list sorted in accending order.
    @pre-condition: num_list must only contain positive integers, b must be integer greater than 2.
    @complexity: best and worst case: O(M(N + b)), where N is total number of integers in input list, M is the number of digits in
    the maximum value in num_list when represented in base b, and b is the base
    """
    if len(num_list) == 0 or len(num_list) == 1: #if list is empty or only has 1 element
        return num_list
    
    no_count_sorts = math.floor(math.log(max(num_list),b) + 1)#calculates number of times counting sort needs to be called
    sorted_list = num_list[:]   #New list for sorting, since input list cannot be modified

    for i in range(0,no_count_sorts + 1): #computes counting sort for every place value from right to left
        sorted_list = counting_sort(sorted_list,b,i)
        

    return sorted_list


def time_radix_sort():
    """
    This function is used to time radix sort for a variety of bases.

    @param: None
    @return: Times: a list containing tuples with a base and time taken for radix sort
             to sort a random list with that specific base.
    @complexity: best and worst case: O(N^2), where N is the number of different bases in list bases.
    """
    test_data = [random.randint(1,(2**64)-1) for _ in range(100000)] #generates random integer list of size 100,000.
    Times = []
    bases = [2,10,50,100,1000,10000] #Bases used for testing

    for i in range(0,len(bases)):
        start = timeit.default_timer() 
        radix_sort(test_data,bases[i])
        end = timeit.default_timer()
        Times.append((bases[i],end-start)) #end-start obtains duration of radix_sort

    return (Times)

def rotate_list(string_list,p):
    """
    This function takes a list of strings and rotates them p times (positive = left)

    @param: string_list: a list of unique strings(a-z), p: number of rotations left/right
    @return: string_list: a rotated version of input list
    @pre-condition: string_list must contain strings and p must be an integer
    @complexity: worst case: O(n),where n is length of string_list best case: O(1), when p == 0
    """
    if p == 0:
        return string_list

    #left rotations
    elif p > 0:
        for i in range(0,len(string_list)):
            rotations = p % len(string_list[i])  #minimises unnecessary rotations
            string_list[i] = string_list[i][rotations:] + string_list[i][:rotations] 

    #right rotations
    elif p < 0:
        p = -(p)
        for i in range(0,len(string_list)):
            rotations = p % len(string_list[i])
            string_list[i] = string_list[i][len(string_list[i])-rotations:] + string_list[i][0:len(string_list[i])-rotations]

    return string_list

def counting_sort_input(string_list,i):
    """
    This is a sub function for find_rotatations, it is used to run counting sort for a part on the input list of strings

    @param: string_list: a list of strings (a-z), i: an integer value > 0, represents the ith call of this function
    @return: string_list: a list of strings sorted at a certain place value
    @pre-condition: string_list must only contain strins a-z, i >= 0
    @complexity: O(N) , where N is the lenth of string_list
    """
    sorting_list = len(string_list) * [0]
    count_arr = [0] * 27

    for k in range(0,len(string_list)):
        index = len(string_list[k]) - i - 1
        if index >= 0:
            pos = ord(string_list[k][index])-96 #index of count array to increment
            count_arr[pos] += 1
        else:
            count_arr[0] += 1

    #adding previous index to current index in count array
    for k in range(1,len(count_arr)):
        count_arr[k] += count_arr[k-1]

    #Makes sorting_list into sorted string_list
    for k in range(len(string_list)-1,-1,-1):
        index = len(string_list[k]) - i - 1
        if index >= 0:
            pos = ord(string_list[k][index])-96
            count_arr[pos] -= 1
            sorting_list[count_arr[pos]] = string_list[k]
        else:
            count_arr[0] -= 1
            sorting_list[count_arr[0]] = string_list[k]



    string_list = sorting_list[:] #copies into string_list
    return string_list
            
def counting_sort_rotated(string_list,i,index_list):
    """
    This is a sub function for find_rotatations, it is used to run counting sort for a part on the rotated list of strings

    @param: string_list: a list of strings (a-z), i: an integer value > 0, represents the ith call of this function,
            index_list: a list of integers representing the original positions of strings in string_list
    @return: string_list: a list of strings sorted at a certain place value, index_list: rearranged version of input
    @pre-condition: string_list must only contain strins a-z, i >= 0
    @complexity: O(N) , where N is the lenth of string_list
    """
    count_arr = [0] * 27
    sorting_list = [0] * len(string_list)
    new_index_arr = [0] * len(index_list)

    for k in range(0,len(string_list)):
        index = len(string_list[k]) - i - 1
        if index >= 0:
            pos = ord(string_list[k][index])-96 #index of count array to increment
            count_arr[pos] += 1
        else:
            count_arr[0] += 1

    #adding previous index to current index in count array
    for k in range(1,len(count_arr)):
        count_arr[k] += count_arr[k-1]

    #Makes sorting_list,new_index_arr into sorted string_list,index_list 
    for k in range(len(string_list)-1,-1,-1):
        index = len(string_list[k]) - i - 1
        if index >= 0:
            pos = ord(string_list[k][index])-96
            count_arr[pos] -= 1
            sorting_list[count_arr[pos]] = string_list[k]
            new_index_arr[count_arr[pos]] = index_list[k]
        else:
            count_arr[0] -= 1
            sorting_list[count_arr[0]] = string_list[k]
            new_index_arr[count_arr[0]] = index_list[k]


    index_list = new_index_arr[:] 
    string_list = sorting_list[:]
    return (string_list,index_list)  
    



def find_rotations(string_list,p):
    """
    This function rotates each string in an input list of strings p times (left = positive) and
    returns list of all strings whos p-rotations also exist in the input list.

    @param: string_list: a list of strings, p: an integer representing the number of rotations
    @return: common_list: a list of strings repsenting the strings in the input list whos p-rotations
             also exist in input_list.
    @pre-condition: string_list must only contain strings containing (a-z), p must be an integer
    @complexity: best and worst case: O(MN) , where M is the maximum letters in a string of string_list
                 and N is the amount of strings in string_list.
    """
    if len(string_list) == 0: #empty list
        return []

    input_list = string_list[:] #not modify list of input
    common_index = []
    rotated_list = rotate_list(input_list[:],p) #creates a list of p-rotations of input_list

    
    index_list = [] #keep tracks of index of items in rotated_list
    for i in range(0,len(string_list)):
        index_list.append(i)

    max_string_length = 0
    for i in range(0,len(string_list)): #finding longest string
        if len(string_list[i]) > max_string_length:
            max_string_length = len(string_list[i])

    for j in range(0,len(string_list)): #one-to-one scan for common strings
        if input_list[j] == rotated_list[j]:
            common_index.append(index_list[j])

    #RADIX SORT for input and rotated lists
    for i in range(0,max_string_length):
        input_list = counting_sort_input(input_list,i)
        rotated_list,index_list = counting_sort_rotated(rotated_list,i,index_list)

        #scan for common strings with one of these conditions
        for j in range(0,len(string_list)):
            if input_list[j] == rotated_list[j]: #Check same index
                common_index.append(index_list[j])
            elif j > 0: #Check index to left
                if input_list[j-1] == rotated_list[j]:
                    common_index.append(index_list[j])
            elif j < (len(string_list)-1): #Check index to right
                if input_list[j+1] == rotated_list[j]:
                    common_index.append(index_list[j])
    
    if len(common_index) == 0: #No Common strings
        return []
    elif len(string_list) > 1:
        common_index = radix_sort(common_index,10) #sort indexes of common strings in assending order
        
    common_index_unique = [common_index[0]]

    #removes duplicate index
    for i in range(0,len(common_index)): 
        if common_index_unique[-1] != common_index[i]:
            common_index_unique.append(common_index[i])
        
    output_list = [] #output list
    for i in range(0,len(common_index_unique)):
        output_list.append(string_list[common_index_unique[i]])

    return output_list




