#       Austin Copley
#       CSCI 102 - Section B
#       Week 10 - Part A

print("Provide the input CSV file name: ")
csv = input("CSVFILE> ")
print("Provide the output PBM file name: ")
pbm = input("PBMFILE> ")

contents = []
height = 0
width = 0

with open(csv, 'r') as csvfile:
        
    file = csvfile.readlines()
    file = list(file)
    
    j = 0
    while j < len(file):
        
        i = 0
        row = list(file[j])
        
        while i < len(row):
            
            if row[i] == ' ' or row[i] == ',':
                row.pop(i)
            i += 1

        width = len(''.join(row))
        row = ' '.join(row)
        contents += row
        j += 1

    height = len(file)

contents = ''.join(contents)
with open(pbm, 'w') as pbmfile:
    pbmfile.write("P1")
    pbmfile.write(f"{width}, {height}")
    pbmfile.write(contents)
print("P1")
print(f"{width}, {height}")
print(contents)
