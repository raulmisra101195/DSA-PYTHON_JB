def pow(a,b):
    MOD = 7
    if(b==0):
        return 1
    ans = pow(a,b//2)
    ans = (ans*ans)%MOD

    if(b%2 == 1) :
        ans = (ans*a)%MOD
    return ans

def pow2(a,b):
    MOD = 7
    if(b == -1):
        b = MOD - 2
    return pow(a,b)
print(pow2(5,-1))