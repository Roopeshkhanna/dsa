class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Function to swap adjacent nodes
def swap(head):
    # Base case: if the list has 0 or 1 node, return as is
    if not head or not head.next:
        return head
    
    new_head = head.next  # The new head after the first swap
    
    prev = None
    curr = head
    
    # Traverse the list and swap adjacent nodes
    while curr and curr.next:
        nxt = curr.next
        pair = nxt.next  # The node after the current pair
        
        # Swapping adjacent nodes
        nxt.next = curr
        curr.next = pair
        
        # If this is not the first swap, connect the previous swapped pair
        if prev:
            prev.next = nxt
        
        # Move prev and curr pointers forward
        prev = curr
        curr = pair
    
    return new_head

# Function to print the linked list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> " if temp.next else " -> null\n")
        temp = temp.next

# Creating the linked list from the array
arr = [1, 2, 3, 4, 5, 6]
head = Node(arr[0])
mover = head

# Populate the linked list
for i in range(1, len(arr)):
    new_node = Node(arr[i])
    mover.next = new_node
    mover = new_node

# Print the original list
print("Original list:")
print_list(head)

# Swap adjacent nodes
swapped_head = swap(head)

# Print the swapped list
print("List after swapping adjacent nodes:")
print_list(swapped_head)
"""class Node {
    int data;
    Node next;

    // Constructor for Node class
    public Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class swapLlRec {
    // Method to swap adjacent nodes using recursion
    private static Node swapAdjacent(Node head) {
        // Base case: if the list is empty or has only one node
        if (head == null || head.next == null) {
            return head;
        }

        // Nodes to be swapped
        Node first = head;
        Node second = head.next;

        // Swap the nodes
        first.next = swapAdjacent(second.next);
        second.next = first;

        // New head of the list
        return second;
    }

    // Method to print the linked list
    private static void printList(Node head) {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data);
            if (temp.next != null) {
                System.out.print("->");
            }
            temp = temp.next;
        }
        System.out.println("->NULL");
    }

    public static void main(String[] args) {
        // Default input values
        int n = 6; // Number of nodes
        int[] values = {1, 2, 3, 4, 5}; // Node values

        // Create the linked list from the default values
        Node head = new Node(values[0]);
        Node mover = head;
        for (int i = 1; i < values.length; i++) {
            Node temp = new Node(values[i]);
            mover.next = temp;
            mover = temp;
        }

        // Print the original list
        System.out.println("Original list:");
        printList(head);

        // Swap adjacent nodes
        head = swapAdjacent(head);

        // Print the modified list
        System.out.println("List after swapping adjacent nodes:");
        printList(head);
    }
}"""