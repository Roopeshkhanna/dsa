#withoutset
arr1=[1,4,2,5,3]
arr2=[7,1,3,4,5]
union=[]
intersection=[]
for i in arr1:
    if i not in union:
        union.append(i)
for i in arr2:
    if i not in union:
        union.append(i)
for i in arr1:
    if(i in arr2):
        intersection.append(i)
print(union)
print(intersection)

