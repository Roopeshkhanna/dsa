a={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s = "MCMXCIV"
sums=a[s[-1]]
pre=sums
for i in range(len(s)-2,-1,-1):
    if(a[s[i]]<pre):
        sums-=a[s[i]]
    else:
         sums+=a[s[i]]

    pre=a[s[i]]
print(sums)