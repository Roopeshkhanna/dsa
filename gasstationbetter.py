import heapq
def sol(arr,k):
     n=len(arr)
     gap=[0]*(n-1)

     pq=[]
     for i in range(n-1):
          dist=arr[i+1]-arr[i]
          heapq.heappush(pq,(-1*(dist),i))
     for j in range(k):
          top=heapq.heappop(pq)
          ind=top[1]
          gap[ind]+=1
          diff=(arr[ind+1]-arr[ind])/(gap[ind]+1)
          heapq.heappush(pq,(-1*diff,ind))
     return(heapq.heappop(pq)[0]*-1)


arr = [1, 2, 3, 4, 5]
k = 4
print(sol(arr,k))
#T.C  O(nlogn + klogn)
#S.C  O(n-1)+O(n-1)