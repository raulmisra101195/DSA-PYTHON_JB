class Solution:
    def countPrimes(self, n: int) -> int:
        if(n<=1):
            return 0
        
        prime_array = [True for i in range(n+1)]
        prime_array[0] = prime_array[1] = False
        for i in range(2,int(math.sqrt(n)+1)):
            if prime_array[i]:
                for j in range(i*i,n+1,i):
                    prime_array[j] = False
        if(prime_array[n] == True):
            return prime_array.count(True) - 1
        else:
            return prime_array.count(True)
