import math
def countPrimes( n,s) :
        p1= [i for i in range(n)]
        p= [True for i in range(n+1)]
        p[0] = p[1] = False
        q = []
     #    print(p1)
        for i in range(2, int(math.sqrt(n)+1)):
            if p[i]:
                for j in range(i*i, n+1, i):
                    p[j] = False
        for i,value in enumerate(p):
            if value:
                q.append(i)
        count = 0
        w = []
     #    print(q)
        for i in range(0,len(q)-1):
             if((q[i] + q[i+1] + 1) in q):
                  count = count + 1
                  w.append(q[i]+ q[i+1]+1)
     #    print(w)
        ans=""
        if(count>=s):
             ans="YES"
        else:
             ans="NO"
        return ans


n,k = map(int, input().split())
print(countPrimes(n,k))