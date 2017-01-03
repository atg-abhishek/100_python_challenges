'''
Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

s = input("Please enter the phrase : ")
lst = s.split(" ")
d = {}
for l in lst:
    if l in d:
        d[l] += 1
    else:
        d[l] = 1
res = []
for k,v in d.items():
    res.append((k,v))
res = sorted(res)
for r in res:
    print(r[0] + " : " + str(r[1]))