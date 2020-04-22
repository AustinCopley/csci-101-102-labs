        #   Austin Copley
        #   ​CSCI 102 – Section B
        #   Week 8 - Part B

print("What are your author names?")
userin = input("NAMES> ")
length = len(userin)
short = []
for i in range(length-1):
    if i < 1:
        short.append(userin[i])
    elif userin[i].isupper() and (userin[i - 1] == "-" and  i > 0):
        short.append(userin[i])
delim = ''
print("OUTPUT", delim.join(short))
