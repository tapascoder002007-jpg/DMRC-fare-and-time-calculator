import math

def display(mins):
    h=(mins//60)% 24
    m=mins%60
    return f"{h:02d}:{m:02d}"

def tomin(h,m): 
    return (h*60)+m

def freq(h):
    if 8<=h and h<10: 
        return 4
    elif 17<=h and h<19: 
        return 4
    else:
        return 8

def nextm(h,m):
    now = tomin(h,m)
    f=freq(h)
    r=now%f
    if r==0:
        return now
    else:
        return now+(f-r)
    
