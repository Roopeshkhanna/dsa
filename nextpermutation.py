gn=[2,1,5,4,3,0,0]

ind=-1
for i in range(len(gn)-2,-1,-2):
    if(gn[i]<gn[i+1]):
        ind=i
        break
if(ind==-1):
        print(gn[::-1])
else:
     for i in range(len(gn)-1,ind,-1):
          if(gn[i]>gn[ind]):
               gn[i],gn[ind]=gn[ind],gn[i]
               break
gn[ind+1:]=gn[:ind:-1]
print(gn)
#T.C O(3n)