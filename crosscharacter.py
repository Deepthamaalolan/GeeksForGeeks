for r in range(int(input())):
    a=input()
    for p in range(len(s)):
        i=len(s)-1
        for q in range(len(s)):
            if(q==p or p+q==i):
                print(a[q],end='')
            else:
                print(" ",end='')
    print()
