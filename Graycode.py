class GrayCode:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        th = self.calc_gray(A)
        return [int(x, 2) for x in th]
        
    def calc_gray(self, bits):
        if(bits == 1):
            return ['1', '0']
        
            
        bit_list = self.calc_gray(bits - 1)
        rev_list = bit_list[::-1]
        bit_list = ['0' + x for x in bit_list]
        #print bit_list
        rev_list = ['1' + x for x in rev_list]
        #print rev_list
        ls =  bit_list + rev_list
        #print ls
        return ls