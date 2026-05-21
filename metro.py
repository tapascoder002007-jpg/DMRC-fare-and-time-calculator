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
        
def outputfn():
    try:
        line=input("Line(Magenta, Blue, Yellow, Grey): ")
        station=input("Station: ").upper()
        current_time=input("Time (HH:MM): ").split(":")
        h=int(current_time[0])
        m=int(current_time[1])

    except ValueError:
        print("Incorrect time format. Please enter as HH:MM ")
        return
    except IndexError:
        print("Incorrect time format. Please use HH:MM.")
        return


    total_min=tomin(h, m)

    if total_min<tomin(6, 0) or total_min>=tomin(23, 0):
        print("No service available (metro runs from 06:00 to 23:00)")
        exit()

    first=nextm(h, m)
    f=freq(h)

    trains=[display(first),display(first + f),display(first + 2*f)]

    print("Next metro at", trains[0])
    print(f"Subsequent metros at {trains[1]}, {trains[2]}, ...")
    return


def l_edges():
    try:
        f=open("metro_data.txt", "r")

    except FileNotFoundError:
        print("File not found.You have to keep the metro file in the same folder as the code file")
        return

    edges=[]
    for line in f:
        parts=line.strip().split(",")
        if len(parts)<5:
            continue
        line_name=parts[0].strip()
        a=parts[1].strip()
        b=parts[2].strip()
        a=a.upper()
        b=b.upper()
        t=int(parts[3].strip())

        edges.append((a,b,t,line_name))
        edges.append((b,a,t,line_name))

    f.close()
    return edges


def buildfn(edges):
    g={}
    for item in edges:
        a=item[0]
        b=item[1]
        t=item[2]
        ln=item[3]
        if a not in g:
            g[a]=[]
            g[a].append((b, t, ln))
        else:
            g[a].append((b, t, ln))
    return g
    

def line(edges,a,b):
    for item in edges:
        s=item[0]
        n=item[1]
        ln=item[3]
        if s==a and n==b:
            return ln
        if s==b and n==a:
            return ln

    return None
    
