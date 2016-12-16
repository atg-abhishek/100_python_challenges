from pprint import pprint 
res = []
for i in range(1000, 3001):
    digits = str(i)
    not_even = False
    for i in range(0,len(digits)):
        if int(digits[i])%2!=0:
            not_even = True
            break
    if not not_even:
        res.append(digits)
pprint(','.join(res))