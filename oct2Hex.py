#Converts an octal number to a hexadecimal number, and returns the result as a string.
num0=[]
num = []
string = []
for i in range(125):
    if i < ord("a") or i > ord("f"):
        continue
    num.append(chr(i))
    print(chr(i))
for i in range(16):
    string.append(str(i))
for i in range(10):
    num0.append(str(i))

num = num0 + num

dictionary = dict(zip(string,num))
for keys in dictionary.keys():
    print(keys,dictionary[keys])
def oct2hex(x:int):
    g = []
    r,q = x %16,x //16
    while q != 0:
        g.append(r)
        r,q = q % 16,q // 16
    g.append(r)
    res = ""
    for i in reversed(g):
        for j in dictionary.keys():
            if i == int(j):
                res += dictionary[j]
    return res


print(oct2hex(62627))