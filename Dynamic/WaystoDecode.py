class WaysToDecode:
    # @param A : string
    # @return an integer
    
    decode_table = {1:'A', 2:'B', 3: 'C', 4: 'D',
                    5:'E', 6:'F', 7: 'G', 8: 'H',
                    9:'I', 10:'J', 11: 'K', 12: 'L',
                    13:'M', 14:'N', 15: 'O', 16: 'P',
                    17:'Q', 18:'R', 19: 'S', 20: 'T',
                    21:'U', 22:'V', 23: 'W', 24: 'X',
                    25:'Y', 26:'Z'}
    result = []
    lookup_table = {}
    
    def numDecodings(self, A):
        #print A
        sub_list1 = []
        sub_list2 = []
        
        
        
        if(not A):
            return ['']
        
        if(A in self.lookup_table.keys()):
            return self.lookup_table[A]
        
        if(len(A) ==1):
            return [self.decode_table[int(A[0])]]
        
        
        
        sub_list = self.numDecodings(A[1:])
        for list_item in sub_list:
            sub_list1.append(self.decode_table[int(A[0])] + list_item)
        
        #print 'sub_list1' + ' '.join([str(x) for x in sub_list1])
        
        if(A[0] == '1' or A[0] == '2'):
            #print '2'
            sub_list = self.numDecodings(A[2:])
            for list_item in sub_list:
                #print self.decode_table[int(A[0] + A[1])]
                sub_list2.append(self.decode_table[int(A[0] + A[1])] + list_item)
        
        #print sub_list1
        #print 'sub_list2' + ' '.join([str(x) for x in sub_list2])
        f = sub_list1 + sub_list2
        self.lookup_table[A] = f
        return f