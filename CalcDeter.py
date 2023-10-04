def msp(i):
    return list(map(int, i.split(" ")))
def msl(i):
    return list(map(str, i.split('!')))
def cds(i,a,b):
    return msp(msl(i)[a])[b]
def BdInStr(l):
    bs=""
    for q in l:
        for w in q:
            bs+=str(w)+' '
        bs=bs[:-1]+'!'
    return bs[:-1]
def oper(s,n):
    if n==2:
        return cds(s,0,0)*cds(s,1,1)-cds(s,0,1)*cds(s,1,0)
    sun=0
    for q in range(n):
        local = []
        for w in msl(s)[1:]:
            localest=[]
            for e in range(n):
                if e!=q:
                    localest.append(msp(w)[e])
            local.append(localest)
        sun+=cds(s,0,q)*(-1)**(q)*(oper(BdInStr(local),n-1))
    return sun
def CalcDeter(L):
    return oper(BdInStr(L),len(L[0]))
