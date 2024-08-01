s = "anagram"
t = "nagarama"
hash = [0] * 26

if len(s) != len(t):
    print(False)
else:
    for i in range(len(s)):
        hash[ord(s[i]) - 97] += 1
        hash[ord(t[i]) - 97] -= 1
    
    for count in hash:
        if count != 0:
            print(False)
            break
    else:
        print(True)
