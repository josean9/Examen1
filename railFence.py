s = input("Enter a string: ")
key = int(input("Enter a key: "))
enc = [
    ["D",0,0,0,"N",0,0,0,"E",0,0,0,"T",0,0,0,"L",0,0],
    [0,"E",0,"E",0,"D",0,"H",0,"E",0,"S",0,"W",0,"L",0,"X",0],
    [0,0,'F',0,0,0,'T',0,0,0,'A',0,0,0,'A',0,0,'X',0]
]
flag = 0
row = 0

for i in range(key):
    enc.append([])
for i in range(len(s)):
    enc[i % key].append(s[i])
for i in range(key):
    print("".join(enc[i]))
