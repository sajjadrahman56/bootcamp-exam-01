name = ["Alice", "Bob", "Charlie", "David", "Eve"]

for i in range(len(name)):
    s = list(name[i])
    if s[0]=='A' or s[0]=='D':
        print(name[i])