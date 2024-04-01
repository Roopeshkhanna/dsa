string = input("Enter the string: ")
dic = {}
start = 0
maxlen = 0
st = 0
culen = 0

for i in range(len(string)):
    if string[i] not in dic:
        dic[string[i]] = i
    else:
        if dic[string[i]] >= st:
            culen = i - st
            if culen > maxlen:
                maxlen = culen
                start = st
            st = dic[string[i]] + 1
    dic[string[i]] = i

if len(string) - st > maxlen: 
    start = st
    maxlen = len(string) - st

print(string[start:start + maxlen])
