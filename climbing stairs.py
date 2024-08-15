def climb(ind,n):
    if(ind>=n-1):
        return(1)
    one=climb(ind+1,n)
    two=climb(ind+2,n)
    return(one+two)
n=3
print(climb(0,n))

"""

or

def climb(ind):
    if(ind<=1):
        return(1)
    one=climb(ind-1)
    two=climb(ind-2)
    return(one+two)
n=3
print(climb(n))


or 


def main():
    n = 3
    prev2 = 1
    prev = 1

    for i in range(2, n+1):
        cur_i = prev2 + prev
        prev2 = prev
        prev = cur_i

    print(prev)

if __name__ == "__main__":
    main()

"""