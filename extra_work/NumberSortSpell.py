def NTW(num,join=True):
    '''strings = {} convert an integer number into strings'''
    ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    second = ['','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    third = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    fourth = ['','Thousand']
    strings = []
    if num == 0: strings.append('Zero')
    else:
        numS = str(num)
        numSLen = len(numS)    
        groups = int((numSLen+2)/3)
        numS = numS.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numS[i]),int(numS[i+1]),int(numS[i+2])
            g = groups-int((i/3+1))
            if h>=1:
                strings.append(ones[h])
                strings.append('Hundred')
            if t>1:
                strings.append(third[t])
                if u>=1: strings.append(ones[u])
            elif t==1:
                if u>=1: strings.append(second[u])
                else: strings.append(third[t])
            else:
                if u>=1: strings.append(ones[u])
            if (g>=1) and ((h+t+u)>0): strings.append(fourth[g])
    if join: return ' '.join(strings)
    return strings

num1, num2 = map(int, input().split())

z = [num1, num2]
while z[0] != z[1]:
    A = sorted(z)
    a1 = NTW(A[0])
    a2 = NTW(A[1])
    d = { a1 : A[0],
          a2 : A[1]
         }
    B = [a1, a2]
    C = sorted(B)
    D = [d[C[0]], d[C[1]]]
#    print("A[0]",A[0])
#    print("A[1]",A[1])
#    print("B[0]",B[0])
#    print("B[1]",B[1])
#    print("C[0]",C[0])
#    print("C[1]",C[1])
#    print("D[0]",D[0])
#    print("D[1]",D[1])
    if D[0] != D[1]:
        z[0] = A[0] + D[0]
        z[1] = A[1] + D[1]
#    print("z[0]",z[0])
#    print("z[1]",z[1])
    if z[0] >= 99999 or z[1] >= 99999:
        print('Out of bounds')
        break
    if z[0] == z[1]:
        print(z[0])
        break
    