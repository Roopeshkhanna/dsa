lis = [1, 1, 2, 2, 3, 4, 100, 101, 102, 103, 104]
s = set(lis)
longest = 0
for num in s:
    if num - 1 not in s:
        x = num + 1
        count = 1
        while x in s:
            x += 1
            count += 1
        longest = max(longest, count)
print(longest)
# T.C O(n+2n)