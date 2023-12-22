import math
T={
    "jam":None,
    "menit":None,
    "detik":None
}
maxDetik=864000
def ResetJam():
    global T
    T["jam"]=0
    T["menit"]=0
    T["detik"]=0
def IsJValid(j,m,d):
    if j>=0 and j<=23:
        return True
    elif m>=0 and m<=59:
        return True
    elif d>=0 and d<=59:
        return True
    else: 
        return False
def MakeJam(jj,mm,dd):
    T={}
    if IsJValid(jj,mm,dd)==True:
        T["jam"]=jj
        T["menit"]=mm
        T["detik"]=dd
        return T 
    else:
        print("Invalid Jam")
def MakeJamTest(jj,mm,dd):
    J=MakeJam(jj,mm,dd)
    TulisJam(J)
def GetHour(T):
    return T["jam"]
def GetMinute(T):
    return T["menit"]
def GetSecond(T):
    return T["detik"]
def SetHH(J,newHH):
    global T
    T["jam"]=newHH
    return T["jam"]
def SetMM(J,newMM):
    global T
    T["menit"]=newMM
    return T["menit"]
def SetSS(J,newSS):
    global T
    T["detik"]=newSS
    return T["detik"]
def BacaJam(J):
    j,m,d=map(int, input("Baca Jam : ").split(":"))
    MakeJam(j,m,d)
def TulisJam(T):
    print("{}:{}:{}".format(T["jam"],T["menit"],T["detik"]))
def Jam2Detik(T):
    return T["jam"]*3600+T["menit"]*60+T["detik"]
def Detik2Jam(N):
    global T
    n1=N
    sisa=0
    if N>maxDetik:
        n1=n1%3600
        jam=n1//3600
        sisa=n1%3600
        menit=sisa//60
        detik=sisa%60
    else:
        jam=n1//3600
        sisa=n1%3600
        menit=sisa//60
        detik=sisa%60
    T["jam"]=jam
    T["menit"]=menit
    T["detik"]=detik
    return T
def JEQ(j1,j2):
    return Jam2Detik(j1)==Jam2Detik(j2)
def JNEQ(j1,j2):
    return Jam2Detik(j1)!=Jam2Detik(j2)
def JLT(j1,j2):
    return Jam2Detik(j1)<Jam2Detik(j2)
def JGT(j1,j2):
    return Jam2Detik(j1)>Jam2Detik(j2)
def JPlus(j1,j2):
    global T
    s=j1["detik"]+j2["detik"]
    m=j1["menit"]+j2["menit"]
    h=j1["jam"]+j2["jam"]
    if s>59:
        T["detik"]=s-60
        m+=1
    else:
        T["detik"]=s
    if m>59:
        T["menit"]=m-60
        h+=1
    else:
        T["menit"]=m
    if h>23:
        T["jam"]=h-24
        print("+1 hari ",end="")
        # TulisJam(MakeJam(h,m,s))
    else:
        T["jam"]=h
        # TulisJam(MakeJam(h,m,s))
    return T
def JMinus(j1,j2):
    global T
    if j1["jam"]>j2["jam"]:
        T["jam"]=j1["jam"]-j2["jam"]
    else:
        T["jam"]=j2["jam"]-j1["jam"]
    if j1["menit"]>j2["menit"]:
        T["menit"]=j1["menit"]-j2["menit"]
    else:
        T["menit"]=j2["menit"]-j1["menit"]
    if j1["detik"]>j2["detik"]:
        T["detik"]=j1["detik"]-j2["detik"]
    else:
        T["detik"]=j2["detik"]-j1["detik"]
    return T
def NextDetik(J):
    global T
    s=J["detik"]+1
    m=J["menit"]
    h=J["jam"]
    if s>59:
        T["detik"]=s-60
        m+=1
    else:
        T["detik"]=s
    if m>59:
        T["menit"]=m-60
        h+=1
    else:
        T["menit"]=m
    if h>23:
        T["jam"]=h-24
        print("+1 hari ",end="")
    else:
        T["jam"]=h
    return T
def NextNDetik(J,N):
    global T
    s=J["detik"]+N
    m=J["menit"]
    h=J["jam"]
    if s>59:
        T["detik"]=s-60
        m+=1
    else:
        T["detik"]=s
    if m>59:
        T["menit"]=m-60
        h+=1
    else:
        T["menit"]=m
    if h>23:
        T["jam"]=h-24
        print("+1 hari ",end="")
    else:
        T["jam"]=h
    return T
def PrevDetik(J):
    global T
    s=J["detik"]-1
    m=J["menit"]
    h=J["jam"]
    if s<0:
        T["detik"]=s+60
        m-=1
    else:
        T["detik"]=s
    if m<0:
        T["menit"]=m+60
        h-=1
    else:
        T["menit"]=m
    if h<0:
        T["jam"]=h+24
        print("-1 hari ",end="")
    else:
        T["jam"]=h
    return T
def PrevNDetik(J,N):
    global T
    s=J["detik"]-N
    m=J["menit"]
    h=J["jam"]
    if s<0:
        T["detik"]=s+60
        m-=1
    else:
        T["detik"]=s
    if m<0:
        T["menit"]=m+60
        h-=1
    else:
        T["menit"]=m
    if h<0:
        T["jam"]=h+24
        print("-1 hari ",end="")
    else:
        T["jam"]=h
    return T
def Durasi(Jaw,Jakh):
    if Jam2Detik(Jakh)<Jam2Detik(Jaw):
        return None
    else:
        return Jam2Detik(Jakh)-Jam2Detik(Jaw)
