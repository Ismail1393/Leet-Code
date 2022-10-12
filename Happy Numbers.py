class Solution:
    def findHappy(self,n : int ) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.squareNumbers(n)
            if n == 1:
                return True
        return False
    
    def squareNumbers(self, n: int) -> int: 
        output = 0
        while n != 0:
            remainder = n % 10 
            remainder = remainder **2 
            output += remainder
            n=n//10
        return output 
    
            