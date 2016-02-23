#Knuth Morriss Prat string searching algorithm

class KMPStrinSearch:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    #Using KMP algorithm
    def preprocessTable(self, needle):
        needle_ls = list(needle)
        table=  []
        table.append(-1)
        i = 1
        leng = 0
        while(i < len(needle_ls)):
            if(needle_ls[i] == needle_ls[leng]):
                leng+= 1
                table.append(leng)
                i+=1
            else:
                if(leng != 0):
                    leng = table[leng - 1]
                else:
                    table.append(leng)
                    i += 1
        return table
            
                    
        
    
    '''
    @param: haystackstr ; main subject string
    @param: needlestr: string to be search
    '''
    def searchString(self, haystackstr, needlestr):
        table =  self.preprocessTable(needlestr)
        #print table
        haystack = list(haystackstr)
        needle = list(needlestr)
        m = 0
        i = 0
        
        while (m + i < len(haystack)):
            if(needle[i] == haystack[m + i]):
                if(i == len(needle) - 1):
                    return m
                i+=1
            else:
                if(table[i] > -1):
                    m = m + i - table[i]
                    i = table[i]
                else:
                    i = 0
                    m = m + 1
        return -1