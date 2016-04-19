def p_bin(x):
    s=''
    while x!=0:
        b=x%2
        x//=2
        s=str(b)+s
    return s
def print_star(m,n)
   for i in range(0,m):
       for j in range(0,n):
           if (j%2==0) and (i%2==0):
