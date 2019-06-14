if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


    #Very noob implication but this is basically what's going down
    ar = []
    i=0
    j=0
    k=0
    while i <= x :
        while j <= y :
            while k <= z :
                if i + j + k != n:
                    ar.append([i,j,k])
                k+=1
            k=0
            j+=1
        i+=1
        j=0
    print (ar)

    #using range and append
    new = []
    for a in range(x+1):
        for b in range(y+1):
            for c in range (z+1):
                if a+b+c !=n:
                   new.append([a,b,c])

    print(new)

    #using list comprehension

    print([[p,q,r] for p in range(x+1) for q in range(y+1) for r in range(z+1) if(p+q+r)!=n])
