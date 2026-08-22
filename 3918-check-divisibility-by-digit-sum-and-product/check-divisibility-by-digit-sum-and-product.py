class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n

        sumof = 0
        prodof = 1

        while num > 0:
            sumof += num % 10
            prodof *= num % 10

            num //= 10
        
        return n % (sumof + prodof) == 0