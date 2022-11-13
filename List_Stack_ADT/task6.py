"""
@author: Abhiram Aroop
@since: 20/09/2019
@modified: 26/09/2019
"""

import task2
import task3

class StackADT:
    def __init__(self):
        """
        Initial Class condition
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and worst case: O(1), constant time complexity
        """
        self.stack = task2.ListADT()

    def size(self):
        """
        This function returns size of stack
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and worst case: O(1), constant time complexity
        """
        return self.stack.length
    
    def is_empty(self):
        """
        This function checks whether the stack is empty
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and worst case: O(1), constant time complexity
        """
        return self.stack.length == 0

    def is_full(self):
        """
        This function checks whether the stack is full
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and worst case: O(1), constant time complexity
        """
        return self.stack.is_full()

    def push(self,item):
        """
        This function appends an item to stack
        :@param: item: any item
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and worst case: O(1), constant time complexity
        """
        self.stack.append(item)

    def pop(self):
        """
        This function pops the last item to stack(LIFO) and returns the item
        :@param: none
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and worst case: O(1), constant time complexity
        """
        if self.is_empty() == False:
            return self.stack.delete(-1)
            
        
class Editor:
    def __init__(self):
        """
        Initial Class condition
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and worst case: O(1), constant time complexity
        """
        self.text_lines = task2.ListADT()
        self.undo_stack = StackADT()

    def read_filename(self, file_name):
        """
        This function reads lines of a text file and copies them to self.text_lines
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and worst case: O(1), constant time complexity
        """
        #Checks whether name of file is a string, if not raise error
        try:
            file_name == str(file_name)
        except (TypeError):
            raise "file_name not string"
        
        #Reads input file and adds lines to self.text_lines
        self.text_lines = task3.read_text_file(file_name)

        
    def print_num(self, line_num = None):
        """
        This function prints a specific or all lines from text_lines
        :@param: line_num, string which holds the line(s) to print 
        :@return: None
        :@pre-condition: line_num can only be string or integer
        :@post-condition: None
        :@complexity: Best case: O(1), when line_num is not None
        :@complexity: Worst case: O(n), where n is length of text_lines, when line_num == None
        """
        if self.text_lines.is_empty() == True:
            print('?')
            raise IndexError
        #prints all elements of self.text_lines, excluding none's
        if line_num == None: 
            for i in range(self.text_lines.length):
                if i != None:
                    print(self.text_lines.the_array[i])
        #prints a line from input
        else:
            if self.text_lines.the_array[int(line_num)-1] != None:
                line_num = int(line_num)-1
                print(self.text_lines.the_array[line_num])
        
    def delete_num(self, line_num = None):
        """
        This function deletes a specific or all lines from text_lines
        :@param: line_num, string which holds the line(s) to delete from array 
        :@return: None
        :@pre-condition: line_num can only be string or integer
        :@post-condition: None
        :@complexity: Best case: O(1), when line_num is not None
        :@complexity: Worst case: O(n), where n is length of text_lines, when line_num == None
        """
        if line_num == "": #Delete All lines?
            #add previous array to undo_stack
            if self.text_lines != task2.ListADT():
                self.undo_stack.push(self.text_lines)
            else:
                self.undo_stack.push(task2.ListADT())
                
            self.text_lines = task2.ListADT()
            
        else:
            try:
                int(line_num)
            except ValueError:
                print('')
                raise ValueError
            #Delete one line
            if int(line_num) < 0 or int(line_num) > self.text_lines.length: #Index Error
                print('?')#Index Error
                raise IndexError
            else:
                #add previous list to undo_stack
                if self.text_lines != task2.ListADT():
                    self.undo_stack.push(self.text_lines)
                else:
                    self.undo_stack.push(task2.ListADT())
            
                self.text_lines.delete(int(line_num)-1) #Deletes the line
            
        

    def insert_num_strings(self, line_num, lines):
        """
        This function inserts line(s) to text_lines
        :@param: line_num, string which tells the line number to add lines
        :@param: lines, list of strings which holds the line(s) to print 
        :@return: None
        :@pre-condition: line_num can only be string or integer, lines can only be a list
        :@post-condition: None
        :@complexity: Best and Worst case: O(n), where n is length of lines
        """
        try:
            int(line_num)
        except ValueError:
            print('?')
            raise ValueError
        line_num = int(line_num)
        
        if self.text_lines != task2.ListADT():
            self.undo_stack.push(self.text_lines)
        else:
             self.undo_stack.push(task2.ListADT())

        #If the line number is -1 when list is empty
        if line_num == -1 and self.text_lines.length == 0:
            line_num = 0 #set line number to first element

            #iterate through each line for the list of lines and inserts to list if its not None
            for line in lines:
                if line != None:
                    self.text_lines.insert(line_num,line)
                    line_num = line_num + 1

            return self.text_lines #return list
        
        #if line number is negative and list not empty
        elif line_num < 0 and self.text_lines.is_empty() == False:
            line_num = self.text_lines.length + line_num
            if line_num < 0: #index range check
                print('?')

            else:            
                #iterate and add all lines to list
                for line in lines:
                    if line != None:
                        self.text_lines.insert(line_num,line)
                        line_num = line_num+1

                return self.text_lines
        
        else: #if line number is positive and not empty
            if line_num > self.text_lines.length+1: #index range check
                raise print('?')

            else:            
                #iterate and add all lines to list
                for line in lines:
                    if line != None:
                        self.text_lines.insert(line_num-1,line)
                        line_num = line_num+1

                return self.text_lines

    def search_string(self, string):
        """
        This function searches for a string in text_lines and returns a list of line number in which the string occurs
        :@param: string: a string
        :@return: str_list: List of line numbers in which the string is found
        :@pre-condition: string must be a string
        :@post-condition: None
        :@complexity: Best and Worst case: O(n), where n is length of the text_lines
        """
        #error
        if str(string) != string:
            print('?')
            return '?'
        str_list = task2.ListADT(40)
        i = 1
        #checking every line of self.text_lines
        for line in self.text_lines:
            if string in line:
                str_list.append(i)
                i += 1

        return str_list

    def undo(self):
        """
        This function restores the previous state of text_lines
        :@param: None
        :@return: None
        :@pre-condition: None
        :@post-condition: None
        :@complexity: Best and Worst case: O(1), constant time complexity
        """
        if self.undo_stack.is_empty() == False:
            self.text_lines = self.undo_stack.pop()
        else:
            raise AssertionError
    
def splitter(string):
    """
    This function converts strings into lists, but splitting the string when there is a space
    :@param: string: a string
    :@return: None
    :@pre-condition: string must be a string
    :@post-condition: None
    :@complexity: Best and Worst case: O(n), where n is length of the string
    """
    command = task2.ListADT()
    empty_str = ""
        
    for letter in (string+' '): #adds extra space to string to set return condition
        if letter != " ": #if not a space, then letter to string
            empty_str = empty_str + letter
        else: #string is a space, append and reset empty string
            command.append(empty_str)
            empty_str = ""
    return command

def quit():
    """
    This function returns True
    :@param: None
    :@return: None
    :@pre-condition: None
    :@post-condition: None
    :@complexity: Best and Worst case: O(1), constant time complexity
    """
    return True

def menu():
    """
    This function runs a ed-style command prompt menu
    :@param: None
    :@return: None
    :@pre-condition: None
    :@post-condition: None
    :@complexity: Best and Worst case: Undetermined, when user input == "quit"
    """
    ed = Editor()
    Quit = False #Loop condition
    while Quit == False: #start Loop
            
        input_command = str(input('Command: ')) #input --> string
        input_command = splitter(input_command) #string --> ListADT()
            
        if input_command.the_array[0] == "read": #if input says to read
            ed.read_filename(input_command.the_array[1])
        elif input_command.the_array[0] == "print": #if input says to print
            ed.print_num(input_command.the_array[1])
        elif input_command.the_array[0] == "insert": #if input says to insert
            lines = task2.ListADT()
            line = str(input("Insert Line: "))
            while line != '.':
                lines.append(line)
                line = str(input("Insert Line: "))
            ed.insert_num_strings(input_command.the_array[1],lines.the_array)
        elif input_command.the_array[0] == "delete": #if input says to delete
            if input_command.length != 1:
                ed.delete_num(input_command.the_array[1])
            else:
                ed.delete_num("")
        elif input_command.the_array[0] == "search": #if input says to search
            string_to_search = input_command.the_array[1]
            for i in range(2,input_command.length):
                string_to_search = string_to_search + ' ' + input_command.the_array[1]
            print(ed.search_string(string_to_search))
        elif input_command.the_array[0] == "undo": #if input says to undo
            ed.undo()
        elif input_command.the_array[0] == "quit": #if input says to quit
            Quit = quit()#ends loop
        else: #unknown input
             print("?")

    print('You have quit')
               

if __name__ == "__main__":
    menu()
        
        

