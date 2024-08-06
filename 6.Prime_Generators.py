import math
def generatePrime(m,n):
    a=[True]*(n+1)
    a[0]=a[1]=False
    l = int(math.sqrt(n))
    for i in range(2,l+1):
        if a[i]:
            for j in range(i*2,l+1,i):
                a[j] = False
    chprime = []
    for i in range(2,l+1):
        if a[i]:
            chprime.append(i)
    
    prime = [True] * (n-m+ 1)

    print(chprime,end=" ")
    for i in chprime:
        lower = (m//i)

        if(lower <= 1):
            lower  = i+i
        elif (m%i) != 0:
            lower  = (lower*i) + i
        else:
            lower = lower*i
        for j in range(lower7,n+1,i):
            prime[j-m] = False
    for k in range(m, n + 1):
	    if prime[k-m]:
		    print(k,end=" ")

generatePrime(15,85)


        
