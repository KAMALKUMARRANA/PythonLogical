string="dkdjs12jdbjsb 7 8gyedgfye8900"
a=[]

for i in range(len(string)):
    for j in string[i]:
        if j.isnumeric():
            a.append(int(j))
print(a)
print(string[0])
