ls=[2,3,4,5,6,2,3,4]
ln=[]
for x in sorted(ls):
    if x not in ln:
        ln.append(x)
print(ln)
for x in sorted(ls):
    if x not in ln:
        ln.append(x)
print(ln)
[2, 3, 4, 5, 6]
