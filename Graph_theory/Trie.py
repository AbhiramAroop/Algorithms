"""
@author: Abhiram Aroop
@since: 10/5/2020
@modified: 25/5/2020
"""
class TrieNode:
    
    def __init__(self):
        """
        Initialising a Node for a Trie, keeping track of the child
        that each Node has and the number of words that exists from the
        Node.

        @param: None
        @return: None
        @complexity: best and worst case: O(1)
        """
        self.node = [None] * 27
        self.count_common_word = 0 #Keeps track of duplicate words
        self.prefix_count = 0 #Keep track of words under the Node

    def __getIndex__(self,char):
        """
        Given a character, this function find the index at which the
        character belongs in TrieNode's list (self.nodes).

        @param: char , a lower case letter in English Alphabets (string of length 1)
        @return: An Integer representing the index that the input character belongs in self.node
        @complexity: best and worst case: O(1)
        """
        return ord(char) - ord("a")

    def insert(self,word):
        """
        This Funtion recursively inserts a string of lower case alphabets into the TrieNode. This is done by
        treating each index of the list of nodes as an unique alphabet based on their ASCII value. This
        function then recursively adds childeren nodes based on their index until all characters of the string
        is inserted into the tree. Since each string also has a '$', this is used to represent the end of the
        word and everytime this character is found, two counters increase in order to keep track of the number
        of common words and total words for the TrieNode.

        @param: word: A string of lower case alphabets with a $ at the end
        @return: None
        @complexity: best and worst case: O(N), where N is the length of the string 
        """
        if word == "$": #End of insertion
            self.count_common_word += 1
            self.prefix_count += 1
            
        else:
            index = self.__getIndex__(word[0])  
            
            if self.node[index] != None: #No previous childern of same character
                self.node[index].insert(word[1:])
            else: #Continue along the tree, the character is already a node
                self.node[index] = TrieNode()
                self.node[index].insert(word[1:])

            self.prefix_count += 1 

    def search_freq(self, word):
        """
        This function finds the amount of times a particular string appears in the TrieNode/Trie. This is
        done by recursively travelling through the representing TrieNode of each characher in the string
        and returnting the counter represting the number of times this word has been inserted, as soon as
        it reaches '$'.

        @param: word: A string of lower case alphabets with a $ at the end
        @return: An integer representing the number of times a string exist in the Trie/TrieNode
        @complexity: best and worst case: O(q), where q is the length of the 'word' string
        """
        
        if word == '$': #Word exist
            return self.count_common_word

        else:
            index = self.__getIndex__(word[0])
            
            if self.node[index] != None: #current character exist, continue along the Trie
                return self.node[index].search_freq(word[1:])

            return 0 #word does not exist
        
        
class Trie:
    def __init__(self,text):
        """
        This is the initialising function of a Trie. It sets the inital root Node to a TrieNode object. It
        takes a list of strings represeting words that need to inserted into the Trie, and inserts them into
        the Trie.

        @param: text: A list of lower case alphabet strings.
        @return: None
        @complexity: best and worst case: O(T), where T is the total number of characters in the string
        """
        self.root = TrieNode()
        
        for i in range(0,len(text)): #Add $ to each string and insert them into Trie
            text[i] += "$"
            self.root.insert(text[i])

    def string_freq(self, query_str):
        """
        This function finds the number of times an input string appears in the Trie, done by calling
        the search_freq method in TrieNode class.

        @param: query_str, a non-empty string of lower case alphabets
        @return: An integer representing the number of times the word appears in the Trie.
        @complexity: best and worst case: O(q), where q is the total number of characters in the input string.
        """
        word = query_str + "$"
        
        return self.root.search_freq(word)


    def prefix_freq(self, query_str):
        """
        This function finds the number of words that a given input string is a prefix of. This is done through
        iterating through each character of the input string, until the TrieNode of the last character is found, then
        returning the counter of the TrieNode representing the number of words that exist within this prefix TrieNode.

        @param: query_str, a non-empty string of lower case alphabets
        @return: An integer representing the number of words that the input string is a prefix of.
        @complexity: best and worst case: O(q), where q is the total number of characters in the input string.
        """
        prefix_str = query_str
        
        for i in range(len(prefix_str)): 

            index = self.root.__getIndex__(prefix_str[i])
            
            if self.root.node[index] == None: #No word in Trie contains prefix
                return 0
            else:
                self.root = self.root.node[index] 

        return self.root.prefix_count

    def strings_pos_wildcard(self, query_str):
        """
        This function splits a given string containing lower case alphabets and one '?'. It splits the
        string appearing before and after the '?' and returns them as a Tuple of two lists.
        
        @param: query_str, a non-empty string of lower case alphabets with one '?'
        @return: An Tuple of two Lists of strings
        @complexity: best and worst case: O(q), where q is the length of the input string
        """

        prefix = []
        suffix = []


        prefix_status = True #Used to keep track the position of character relative to the wildcard

        #Sepratates the query_str into two parts
        for i in range(0,len(query_str)):
            #Strings before '?' in query_str
            if query_str[i] != '?' and prefix_status == True: 
                prefix.append(query_str[i])
            elif query_str[i] == '?':
                prefix_status = False
            #Strings after '?' in query_str
            else:
                suffix.append(query_str[i])


        return prefix,suffix

    def merge_strings(self,lst):
        """
        This function combines all strings, given a list of strings
        
        @param: lst, a list of strings
        @return: merged_string: A string that is the combined string of all strings in lst
        @complexity: best and worst case: O(l), where l is the length of the list lst.
        """
        
        merged_string = ""
        
        for string in lst:

            merged_string += string

        return merged_string


    def wildcard_prefix_freq(self, query_str):
        """
        This function takes input a string of lower case alphabets with a '?' representing the
        wildcard. This function finds all the possible characters that could take the place of
        the wildcard, such that it belongs in the Trie. Then it returns a list of all the words
        that can be formed by replacing the wildcard.

        @param: query_str: A string of lower case alphabets and a '?'
        @return: wildcard_sol: A list of strings representing words that could be made
                               by replacing the wildcard, given that the word is in the Trie
        @complexity: O(q + S), where q is the length of the input string and S is the combined
                               length of all the strings stored in the Trie.
        """

        wildcards_sol = []

        prefix,suffix = self.strings_pos_wildcard(query_str)

        
        pre_str = self.merge_strings(prefix) #string before '?'
        post_str = self.merge_strings(suffix) #string after '?'


        wildcard_node = self.root 

        #Find the parent Node of the of the wildcard
        for i in pre_str:
            print(wildcard_node.node)
            index = self.root.__getIndex__(i)+1

            if wildcard_node.node[index] != None:
                wildcard_node = wildcard_node.node[index]


        #Overall string made from wildcard
        for i in range(0,26):

            if wildcard_node.node[i] != None:
                wildcards_sol.append(pre_str + chr(i + ord("a")) + post_str)
                        

        return wildcards_sol
        


    
