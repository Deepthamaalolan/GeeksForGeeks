for r in range(int(input())):
    a=input()
    for p in range(len(a)):
        i=len(a)-1
        for q in range(len(a)):
            if(q==p or p+q==i):
                print(a[q],end='')
            else:
                print(" ",end='')
    print()
    
