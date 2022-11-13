"""
@author: Abhiram Aroop
@since: 15/09/2019
@modified: 19/09/2019
"""

import math 
class ListADT:
    def __init__(self,size=None):
        """
        This function initialises the ListADT, creates the array based on input size.
        @:param: size, an integer
        @:return: none
        @:pre-conditions: size must be an integer > 0
        @:post-conditions: none
        @:complexity: best and worst case: O(n), where n is input size
        """
        if size == None:
            size = 40
        self.length = 0
        self.the_array = [None] * size #array = [None,None,...]
            
        if size < 40:
            size = 40
        self.length = 0
        self.the_array = [None] * size #array = [None,None,...]

    def __str__(self):
        """
        This function converts items of the array into a string
        @:param: none
        @:return: none
        @:pre-conditions: none
        @:post-conditions: none
        @:complexity: best and worst case: O(n), where n is the size of the array 
        """
        string = ''
        newline_str = '\n'

        #empty list?
        if self.length == 0:
            return string

        string = str(self.the_array[0])

        #adds the next item in a new line for string
        for i in range(1,self.length): 
            string = string + newline_str + str(self.the_array[i])

        return string

    def __len__(self):
        """
        This function finds the length of the array
        @:param: none
        @:return: self.length, length of occupied list
        @:pre-conditions: none
        @:post-conditions: none
        @:complexity: best and worst case: O(1), as constant value
        """
        return self.length

    def __getitem__(self,index):
        """
        This function returns the item at the input index
        @:param: index, an integer
        @:return: self.the_array[index], item in the index of input
        @:pre-conditions: index must be an integer between -self.length and self.length-1
        @:post-conditions: none
        @:complexity: best and worst case: O(1), constant time
        """
        #checking pre-conditions for index
        try:
            assert index == int(index)
            assert -self.length <= index <= self.length-1
        except (AssertionError, ValueError):
            raise IndexError('index not within range')
            raise AssertionError('index not integer')

        #making index a positive value, as it will start from last element of the_array if negative
        if index < 0:
            index = self.length + index

        return self.the_array[index]

    def __setitem__(self,index,item):
        """
        This function replaces the item at the input index with input item
        @:param: index, an integer
        @:param: item
        @:return: none
        @:pre-conditions: index must be an integer between -self.length and self.length-1
        @:post-conditions: none
        @:complexity: best and worst case: O(1), constant time
        """
        #checks for errors
        try:
            assert index == int(index)
            assert (0 <= index <= self.length-1) or (1-self.length <= index <= -1)
        except (AssertionError, ValueError):
            raise IndexError('index not within range')
            raise AssertionError('index not integer')
        
        if index < 0:
            index = self.length + index

        self.the_array[index] = item

    def __eq__(self,other):
        """
        This function checks whether the list is the same as another input list
        @:param: other, an array
        @:return: True or False, Boolean value, depending on whether the two lists are the same
        @:pre-conditions: if other is not a ListADT object, False will be returned
        @:post-conditions: none
        @:complexity: best and worst case: O(n), where n is size of current list or other.
        """
        if type(other) != type(self): #checking same type
            return False

        if self.length >= other.length: #if self.length has greater or equal length
            for i in range(0,self.length): #check elements within size of list
                if self.the_array[i] != other.the_array[i]:
                    return False
            for i in range(0,self.length): #other elements can only be None
                if self.the_array[i] != None:
                    return False
        else:
            for i in range(0,other.length): #checks elements with other.len()
                if self.the_array[i] != other.the_array[i]:  #same item?
                    return False     
            for i in range(other.length,len(other)): #other elements can only be None
                if other.the_array[i] != None: #same item?
                    return False 
        return True



    def insert(self,index,item):
        """
        This function inserts the input item at the input index
        @:param: index, an integer
        @:param: item
        @:return: none
        @:pre-conditions: index must be an integer between -self.length-1 and self.length-1
        @:post-conditions: none
        @:complexity: best case: O(1), when index at end of list
        @:complexity: worst case: O(n), where n is size of list, when index is at start of list
        """
        try:
            assert index == int(index)
            assert (0 <= index <= self.length) or (-self.length-1 <= index <= -1)
        except (AssertionError, ValueError):
            raise IndexError('index not within range')
            raise AssertionError('index not integer')

        if self.is_full(): #increment array size
            self.the_array = self.the_array + [None]*(math.ceil(len(self.the_array)*1.9-len(self.the_array)))

        if index < 0: #changing index to positive
            index = self.length + index

        self.length += 1

        for i in range(self.length-1,index,-1): #moving each element
            self.the_array[i+1] = self.the_array[i]
 
        self.the_array[index] = item #adding new element

    def delete(self,index):
        """
        This function deletes the item at input index and returns it
        @:param: index, an integer
        @:return: self.the_array[index], item in the index of input
        @:pre-conditions: index must be an integer between -self.length and self.length-1
        @:post-conditions: none
        @:complexity: best case: O(1), when index at end of list
        @:complexity: worst case: O(n), where n is size of list, when index is at start of list
        """
        try:
            assert index == int(index)
            assert (0 <= index <= self.length-1) or (-self.length <= index <= -1)
        except (AssertionError, ValueError):
            raise IndexError('index not within range')
            raise AssertionError('index not integer')
            
        delitem = self.the_array[index]

        if index < 0: #changing index to positive
            index = self.length + index

        delitem = self.the_array[index]
        for i in range(index,self.length-1): #moving elements
            self.the_array[i] = self.the_array[i+1]


        self.length -= 1 #reduce size

        if len(self.the_array) < 40:
            self.append(None)

        #decreases array size if the conditions match
        if (self.length < (len(self.the_array)/4)) and len(self.the_array)/2 >= 40: 
            new_array = [None]*(len(self.the_array)//2)
            for i in range(0,len(self.the_array)//2):
                new_array[i] = self.the_array[i]
            self.the_array = new_array
            
        return delitem

        
    def is_empty(self):
        """
        This function checks whether the list is empty
        @:param: none
        @:return: True or False, Boolean value, depending on whether list is empty
        @:pre-conditions: none
        @:post-conditions: none
        @:complexity: best and worst case: O(1)
        """
        return self.length == 0

    def is_full(self):
        """
        This function checks whether the list is full
        @:param: none
        @:return: True or False, Boolean value, depending on whether list is full
        @:pre-conditions: none
        @:post-conditions: none
        @:complexity: best and worst case: O(1)
        """
        return self.length == len(self.the_array)

    def __contains__(self, item):
        """
        This function checks whether the list contains input item
        @:param: item
        @:return: True or False, Boolean value, depending on whether list is full
        @:pre-conditions: none
        @:post-conditions: none
        @:complexity: best and worst case: O(n), n is size of list
        """
        for i in range(self.length): #checking every element of list
            if item == self.the_array[i]:
                return True
        return False
 
    def append(self, item):
        """
        This function appends an item to the array
        @:param: item
        @:return: none
        @:pre-conditions: none
        @:post-conditions: none
        @:complexity: best and worst case: O(1)
        """
        if not self.is_full(): #if list is not full
            self.the_array[self.length] = item
            self.length +=1
        else:
            raise Exception('List is full')

	
    def unsafe_set_array(self,array,length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        try:
            assert self.in_test_mode
        except:
            raise Exception('Cannot run unsafe_set_array outside testing mode')
			
        self.the_array = array
        self.length = length


if __name__ == '__main__':
    li = ListADT(10)
    #li.append(1)
    #li.append(1)
    #print(li.delete(0))
