"""
Name: Abhiram Aroop
Student ID: 30632714
"""
import sys

#huffman tree setup
class huffman_node:
    def __init__(self,freq,char,left=None,right=None):
        self.left = left
        self.right = right
        self.char = char
        self.freq = freq

        self.huffman_code = ''


def getNode(node,L, val = ''):
    new_val = val + str(node.huffman_code)

    #traveerse and find node
    if (node.left):
        getNode(node.left,L, new_val)
    if (node.right):
        getNode(node.right,L, new_val)
    if (not node.left and not node.right):
        L[ord(node.char)-10] = new_val


def set_nodes(chars, freq):
    nodes = []
    L = []

    for i in range(118):
        L.append(0)

    for x in range(len(chars)):
        nodes.append(huffman_node(freq[x],chars[x]))

    #set up for huffman tree
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes[0]
        right = nodes[1]

        left.huffman_code = 0
        right.huffman_code = 1
        
        #set up a new node
        newNode = huffman_node(left.freq+right.freq,left.char+right.char,left,right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    #finds the huffman nodes from nodes[0]
    getNode(nodes[0],L)

    return L

#get the list of chars and corresponding freqs of string
def get_char_freqs(string):
    char_ascii = []
    
    #size = 127-32+1(for newling string aswell)
    for i in range(0,97):
        char_ascii.append(0)

    for i in string:
        #special case
        if i == "\n":
            char_ascii[-1] += 1
        else:
            char_ascii[ord(i)-33] += 1

    chars = []
    freqs = []

    #only using 97 vals ranging plus ascii of 10
    for i in range(0,97):
        if char_ascii[i] > 0:
            if i == 96:
                chars.append("\n")
            else:
                chars.append(chr(i+33))
            freqs.append(char_ascii[i])

    return chars, freqs

def get_binary_char(chars):
    bin_vals = []

    #get binary values of corresponding chars in a list
    for char in chars:
        ascii_val = ord(char)
        bin_val = bin(ascii_val)
        bin_vals.append(bin_val)

    return bin_vals

#binary elias omega code encoder
def elias_code(n):
    if n == 1:
        return bin(n)[2:]

    string_bin = bin(n)[2:]

    while n > 1:
        
        L = bin(n)[2:]
        n = len(L) - 1

        #end if n = 1
        if n != 1:
        
            bin_n = bin(n)[2:]
            new_bin = ""

            #find next bits
            for i in range(0,len(bin_n)-1):
                new_bin += '0'

            if bin_n[-1] == '1':
                new_bin += '1'
            else:
                new_bin += '0'

            string_bin = new_bin + string_bin
            
    #leading 0 bit added
    string_bin = "0" + string_bin
    
    return string_bin
    

def huffman_encoding(string):
    #get all huffman and elias code values
    chars, freq = get_char_freqs(string)
    huffman_codes = set_nodes(chars,freq)
    elias_length = elias_code(len(chars))
    elias_chars = []

    encoding = elias_length

    #encode all chars
    for char in chars:
        ascii_char = ord(char)
        huff_length = len(huffman_codes[ascii_char-10])
        elias_val = elias_code(huff_length)
        elias_chars.append(elias_val)

    #combine encoded chars into string
    for i in range(len(chars)):
        ascii_string = str(bin(ord(chars[i]))[2:])
        while len(ascii_string) != 7:
            ascii_string = '0' + ascii_string
        
        encoding = encoding + ascii_string + elias_chars[i] + huffman_codes[ord(chars[i])-10]
    

    return encoding

def read_file_to_string(txt_file):
    f = open(txt_file,"r")

    f_lines = f.readlines()
    string = ""

    for line in f_lines:
        string += line    
    
    return string

def writeout(output):
        
    f = open("output_header.txt","w+")
    f.write(output)
    f.close()


if __name__ == "__main__":
    input_file = str(sys.argv[1])
    input_str = read_file_to_string(input_file)
    output = huffman_encoding(input_str)
    writeout(output)


