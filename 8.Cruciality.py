def crucialEquation(a,b,c):


    while(a != 0 and b != 0):
        if(a>=b):
            a=a-b

        else:
            b=b-a
    
    if a==0: ans=b 
    else: ans=a

    if(c%ans==0):
        return "YES"
    else:
        return "NO"

print(crucialEquation(3,6,7))