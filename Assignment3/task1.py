s = list("aebecedefeg")
for i in range(len(s)):
    if(s[i] == 'e'):
        s[i]='E'
s = "".join(s)
print(s)
