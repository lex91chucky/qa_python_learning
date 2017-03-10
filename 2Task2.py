s = "We are not what we should be! \nWe are not what we need to be. \nBut at least we are not what we used to be \n(Football Coach)"
print(s)
s1 = s.split()
print(s1)
print(len(s1))

s1.sort()

for i in s1:
    i=i.strip("!,().")
    print(i)

d = {}
for i in s1:
    i=i.strip("!,().")
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)



