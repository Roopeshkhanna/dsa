 largest = float("-inf")
    slargest = float("-inf")
    re = []
    smallest = float("inf")
    ssmallest = float("inf")

    for i in range(n):
        if largest < a[i]:
            slargest = largest
            largest = a[i]
        elif a[i] < largest and a[i] > slargest:
            slargest = a[i]

    for i in range(n):
        if smallest > a[i]:
            ssmallest = smallest
            smallest = a[i]
        elif smallest < a[i] and a[i] < ssmallest:
            ssmallest = a[i]
