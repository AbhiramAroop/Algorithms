"""
Name: Abhiram Aroop
Student ID: 30632714
"""
import sys

#function to decode elias omega binary string
def elias_decoder(s):
    if s[0] == '1':
        return 1,1
   
    start = 1
    count = 1
    #how much of the original string did we use?
    end = 3

    #run until leading bit is 1
    while s[start] != "1":
        bit_str = "1"
        for i in range(start + 1, end):
            bit_str += s[i]

        #count the amount of bits to skip
        count = int(bit_str,2) + 1
        start = end
        end += count

    #integer of the obtained bit value
    result = int(s[start:end],2)

    return result,end

#function to find the char corresponding within the huffman code in the next k bits
def check_huffman(s,huffman_codes,chars):
    #test out all huffman codes to see which one works
    #huffman codes are anti prefix, so one is not a prefix of other
    for i in range(len(huffman_codes)):
        str_len = len(huffman_codes[i])
        if s[:str_len] == huffman_codes[i]:
            #return the match!
            return chars[i],str_len
        
    

def decoder(string):
    #finds the number of unique chars from header
    #and the starting pos of next part of header
    unique_char_num,char_index = elias_decoder(string)
    chars = []
    huffman_codes = []
    freqs = []
    
    #extract info from header
    for i in range(0,unique_char_num):
        char_bit = string[char_index:char_index+7] 
        chars.append(chr(int(char_bit,2)))
        char_index += 7

        #find the length of the huff man code ans skips the corresponding bits
        huff_length,add_index = elias_decoder(string[char_index:])
        char_index += add_index
        
        huffman_codes.append(string[char_index:char_index+huff_length])
        char_index += huff_length

    #extract from data section of binary string
    no_format_fields,add_char = elias_decoder(string[char_index:])         
    char_index += add_char

    format_field = []

    #get format fields data 
    for i in range(0,no_format_fields):
        format_field.append([])
        format_field[i].append(int(string[char_index]))
        char_index += 1

        #is the bit 0 or 1?
        if format_field[-1][0] == 0:
            #finds the 2 integers
            next_val,add_val = elias_decoder(string[char_index:])
            char_index += add_val
            format_field[-1].append(next_val)
            
            next_val,add_val = elias_decoder(string[char_index:])
            char_index += add_val
            format_field[-1].append(next_val)

        elif format_field[-1][0] == 1:
            #finds the corresponding huffman code
            huffman_char,add_val = check_huffman(string[char_index:],huffman_codes,chars)
            format_field[-1].append(huffman_char)
            char_index += add_val

    #final decoded string
    output_string = ""

    #put all the data gathered to form the string
    for i in range(0,len(format_field)):

        #1 represents the char
        if format_field[i][0] == 1:
            output_string += format_field[i][1]

        #0 represents a repeating pattern
        elif format_field[i][0] == 0:
            n_match = format_field[i][1]
            n_length = format_field[i][2]

            start_char = len(output_string)-n_match
            #add repeating chars to output string
            for j in range(0,n_length):
                current_char = output_string[start_char+j]
                output_string += current_char
                
        
    
    return output_string

def read_file_to_string(txt_file):
    f = open(txt_file,"r")

    f_lines = f.readlines()
    string = ""

    for line in f_lines:
        string += line
    
    return string

def writeout(output):
        
    f = open("output_decoder_lzss.txt","w+")
    f.write(output)
    f.close()


if __name__ == "__main__":
    bin_str_file = str(sys.argv[1])
    bin_str = read_file_to_string(bin_str_file)

    output = decoder(bin_str)
    writeout(output)
    



