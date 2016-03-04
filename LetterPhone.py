class LetterPhone:
    
    
    def compare(item1, item2):
        if((item1 == 0 and item2 == 1)):
            return 1
        elif(item1 == 1 and item2 == 0):
            return -1
        else:
            if (item1 < item2):
                return -1
            elif(item1 > item2):
                return 1
            else:
                return 0
            
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        letter = {'0': ['0'], '1': ['1'], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], 
                  '4':['g', 'h','i'], '5':['j', 'k', 'l'], 
                  '6':['m', 'n', 'o'], '7':['p', 'q', 'r' , 's'],
                  '8': ['t','u', 'v'], '9':['w', 'x', 'y', 'z']}
    
        
        A = ''.join(sorted(A, key=self.compare))
        
        
        
        return self.join(A, letter)
        
    def join(self, A, letter):
        
        if(len(A) == 1):
            return letter[A[0]]
        
        ret = []
        lower_list = self.join(A[1:], letter)
        temp = letter[A[0]]
        for i in temp:
            for j in lower_list:
                ret.append(i + j)
        
        return ret
            
        
