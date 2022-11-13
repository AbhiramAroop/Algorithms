"""
@author: Abhiram Aroop
@since: 15/09/2019
@modified: 19/09/2019
"""

from task2 import ListADT


def read_text_file(name):
    """
    This reads a text file and copies each line into an array
    @:param: name, name of file
    @:return: List, a ListADT consisting of lines of the read file as items
    @:pre-conditions: name must be a valid file name
    @:post-conditions: List is ListADT, use class ListADT to modify List
    @:complexity: best and worst case: O(n), n is number of lines of file(name)
    """
    name = str(name)
    file = open(name,"r") #open file
    read_lines = file.readlines()

    List = ListADT(40)

    #copies each line into List
    for line in read_lines: 
        List.append(line)

    file.close() #close file
    return List

#Test
name = "TestFile.txt"
read_text_file(name)



