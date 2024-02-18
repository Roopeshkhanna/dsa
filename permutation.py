import math as p

num = 1234
original_num = num
result = []
digits = int(p.log10(num)) + 1

while True:
    last_digit = num % 10
    remaining_digits = num // 10
    num = last_digit * pow(10, digits - 1) + remaining_digits
    result.append(num)
    if num == original_num:
        break

print(result)
#T.C(n)