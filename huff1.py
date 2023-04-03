import heapq
import os
   
class Huffman:
    def __init__(self,path):
        self.path = path
        self.heap = []
        self.make_codes = {}

    class binaryTreeNode:

        def __init__(self,char,freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None


        def __lt__(self,other):
            if other == None:
                return False
            if (not isinstance(other,Huffman.binaryTreeNode)):
                return False
            return self.freq < other.freq
        
        """
        def __eq__(self,other):
            if other == None:
                return False
            if (not isinstance(other,Huffman.binaryTreeNode)):
                return False
            return self.freq == other.freq
        """
    def __inputFrequency(self,text):
        freqDictionary = {}
        for i in text:
            if i not in freqDictionary:
                freqDictionary[i] = 0 
            freqDictionary[i] += 1
        return freqDictionary
    
    def __buildHeap(self,freqDictionary):
        for key in freqDictionary:
            frequency = freqDictionary[key]
            node = self.binaryTreeNode(key,frequency)
            heapq.heappush(self.heap,node)
        
    def buildBinaryTree(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            freqSum = node1.freq + node2.freq
            newnode = self.binaryTreeNode(None,freqSum)
            newnode.left = node1
            newnode.right = node2
            heapq.heappush(self.heap,newnode)
        
    def buildCodeHelper(self,Node,currentCode):
        #base
        if Node == None:
            return
        #logic
        if Node.char != None:
            self.make_codes[Node.char] = currentCode
        self.buildCodeHelper(Node.left,currentCode + "0")
        self.buildCodeHelper(Node.right,currentCode + "1")
        
    def buildCode(self):
        root = heapq.heappop(self.heap)
        currentCode = ""
        self.buildCodeHelper(root,currentCode)

    def getEncodedText(self,text):
        encodedText = ""
        for charac in text:
            encodedText += self.make_codes[charac] 
        return encodedText

    def compression(self):
        filename,fileExtension = os.path.splitext(self.path)
        outputPath = filename + ".bin"
        
        with open(self.path, 'r') as file, open(outputPath, 'wb',) as output:
            text = file.read()
            #text = 'abc'
            text = text.rstrip()

        #convert text to frequency map
        freqDictionary = self.__inputFrequency(text)
        #build minheap
        Heap = self.__buildHeap(freqDictionary)
        #build binary tree from heap
        self.buildBinaryTree()
        #build freq map of code
        self.buildCode() 
        #encode the text based on frequency map
        encoding = self.getEncodedText(text)
        print("encoded Text = ", encoding)

if __name__ == "__main__":
    path = "./sample.txt"
    code = Huffman(path)
    code.compression()
