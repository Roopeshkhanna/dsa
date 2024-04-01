str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
dic = {}

if len(str1) != len(str2):
    print("Strings are not isomorphic")
else:
    for i in range(len(str1)):
        if str1[i] in dic:
            if dic[str1[i]] != str2[i]:
                print("Strings are not isomorphic")
                break
        else:
            dic[str1[i]] = str2[i]
    else:
        print("Strings are isomorphic")
