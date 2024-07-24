import math

def countPrimes(n):
    if(n<=1):
        return 0
    prime_array = [True for i in range(n+1)]
    prime_array[0] = prime_array[1] = False
    for i in range(2,int(math.sqrt(n)+1)):
        if prime_array[i]:
            for j in range(i*i,n+1,i):
                prime_array[j] = False
        
    for i in range(2,n+1):
        print(i,"-->",end=" ")
        for j in range(len(prime_array)):
            if(i < j):
                break
            else:
                if(prime_array[j] == True):
                    print(j, end=" ")
        print("\n")

n = int(input("Enter a number"))
countPrimes(n)

    
    
