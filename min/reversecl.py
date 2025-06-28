class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Function to convert an array into a circular linked list
def arr_to_cl(arr, n):
    head = Node(arr[0])
    mov = head
    for i in range(1, n):
        temp = Node(arr[i])
        mov.next = temp
        mov = temp
    mov.next = head  # Make the list circular
    return head

# Recursive function to reverse a circular linked list
def reverse(head):
    prev =None
    current=head
    start=head
    while(True):
        ne=current.next
        current.next=prev
        prev=current
        current=ne
        if(current==start):
            break
    return( )
# Function to print the circular linked list
def print_circular_linked_list(head):
    if head is None:
        return
    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()

# Input the number of elements in the list and the list of elements
n = int(input())
lis = list(map(int, input().split()))

# Create the circular linked list from the array
head = arr_to_cl(lis, n)

# Reverse the circular linked list
head = reverse(head)

# Print the reversed circular linked list
print("Reversed Circular Linked List:", end=" ")
print_circular_linked_list(head)
