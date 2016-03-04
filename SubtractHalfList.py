class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        result = head = last  = A
        length = 0
        while(A):
            length += 1
            A = A.next
            
        mid = (length/ 2) + (length % 2)
        cntr = 1
        ls = []
        while(last):
            if(cntr > mid):
               ls.append(int(last.val))
            last = last.next
            cntr+=1
            
        ls.reverse()    
        #print ls
        while(ls):
            head.val = ls.pop(0) - int(head.val)
            head = head.next
            
        #self.debug(result)    
        #while(i != j)
        return result
    
    
    def debug(self, A):
        strn = ''
        while(A):
            strn += str(A.val) + ' '
            A = A.next
            
        print strn
