class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def arrtoll(arr, n):
    head = node(arr[0])
    temp = head
    for i in range(1, n):
        new_node = node(arr[i])
        temp.next = new_node
        temp = new_node
    return head

def reverse(head):
    if head is None or head.next is None:
        return head
        
    newhead = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newhead

def modify(head):
    temp = head
    if head is None or head.next is None:
        return head
    
    maxi = float("-inf")
    dummy = node(-1) 
    mov = dummy
    
    while temp is not None:
        if temp.data >= maxi:
            maxi = temp.data
            dummy.next = temp
            dummy = temp
        temp = temp.next
    
    dummy.next = None  
    return mov.next


le = int(input("Enter the number of elements in the list: "))
lis = list(map(int, input(f"Enter {le} integers separated by space: ").split()))


head = arrtoll(lis, le)
head = reverse(head)
head = modify(head)

temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next
