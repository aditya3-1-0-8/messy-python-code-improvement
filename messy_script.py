# ORIGINAL messy version (kept for comparison)
d=[("aditya",92),("riya",85),("kabir",58),("neha",71)]
t=0
for i in range(len(d)):
    t=t+d[i][1]
a=t/len(d)
print("avg",a)
for i in range(len(d)):
    if d[i][1]>=90:
        print(d[i][0],"A")
    else:
        if d[i][1]>=75:
            print(d[i][0],"B")
        else:
            if d[i][1]>=60:
                print(d[i][0],"C")
            else:
                print(d[i][0],"F")
