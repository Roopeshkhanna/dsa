class node:
    def __init__(self, co, ex, next=None):
        self.co = co  # coefficient
        self.ex = ex  # exponent
        self.next = next  # pointer to the next node
ch='y'
cnt=1
dummy1=node(0,0)
dummy2=node(0,0)
temp1=dummy1
temp2=dummy2
def add(head):
    result = node(0, 0)
    temp2 = head
    re = result

    while temp2:
        current = result
        found = False
        while current.next:
            if current.next.ex == temp2.ex:
                current.next.co += temp2.co
                found = True
                break
            current = current.next
        if not found:
            if temp2.co != 0:
                new_node = node(temp2.co, temp2.ex)
                current.next = new_node
        temp2 = temp2.next

    return result.next

def multiply(p1, p2):
    dummy = node(0, 0)
    temp = dummy
    temp1 = p1

    while temp1:
        temp2 = p2
        while temp2:
            coeff = temp1.co * temp2.co
            power = temp1.ex + temp2.ex
            if coeff != 0:
                new_node = node(coeff, power)
                temp.next = new_node
                temp = new_node
            temp2 = temp2.next
        temp1 = temp1.next

    head = add(dummy.next)
    return head

def printing(head):
    temp = head
    first = True
    output = []

    while temp:
        if not first:
            if temp.co > 0:
                output.append(" +")
            else:
                output.append(" ")
        if temp.ex == 0:
            output.append(f"{temp.co}")
            break
        else:
            if temp.co == 1:
                if temp.ex == 1:
                    output.append("x")
                else:
                    output.append(f"x^{temp.ex}")
            elif temp.co == -1:
                if temp.ex == 1:
                    output.append("-x")
                else:
                    output.append(f"-x^{temp.ex}")
            else:
                if temp.ex == 1:
                    output.append(f"{temp.co}x")
                else:
                    output.append(f"{temp.co}x^{temp.ex}")
        temp = temp.next
        first = False

    print(''.join(output))

def read_polynomial(dummy_node):
    temp = dummy_node
    while True:
        val = list(map(int, input().split()))
        ch = input()
        node_val = node(val[0], val[1])
        temp.next = node_val
        temp = node_val
        if ch == 'n':
            break

# Read first polynomial
read_polynomial(dummy1)

# Read second polynomial
read_polynomial(dummy2)

# Perform multiplication and print result
head = multiply(dummy1.next, dummy2.next)
printing(head)
