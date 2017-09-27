n=input()
l=map(int,raw_input().strip().split())
l.sort()
w=l[0]
s=w+4
count=1
for i in l:
    if i>=w and i<=s:
        continue
    else:
        w=i
        s=w+4
        count+=1

print count
