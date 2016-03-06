class CatalanNumber:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        self.output = set()
        self.generate(A, ['('])
        return sorted(self.output)
    
    
    def generate(self, n, braces):
        if len(braces) == 2*n:
            self.output.add(''.join(braces))
            return

        if braces.count('(') < n:
            self.generate(n, braces + ['('])

        if braces.count(')') < braces.count('('):
            self.generate(n, braces + [')'])