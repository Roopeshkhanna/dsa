class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=self.left
pre=[8,5,1,7,10,12]
def construct(lis,bound,i):
    if(len(lis)<i or lis[i]>bound):
        return
    node=Node(lis[i])
    i[0]+=1
    node.left=construct(lis,node.data,i)
    node.right=construct(lis,bound,i)
    return(node)
node=construct(pre,float("inf"),0)
