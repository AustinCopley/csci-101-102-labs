        #   Austin Copley
        #   ​CSCI 102 – Section B
        #   Week 5B - It's Full of Stars

input_string = input("INPUT> ")
input_string = input_string.replace(" ", "_")
input_list = list(input_string)
length = len(input_list)
new_list = []
i = 1

while i <= length:
    if i < length:
        new_list.append(input_list[i-1])
        new_list.append(" ")
    elif i == length:
        new_list.append(input_list[i-1])
    i += 1

empty = ""
new_string = empty.join(new_list)
new_length = len(new_string)

rows = length
i = 1
stars = 1
while stars <= rows:
    while i <= stars:
        if stars == 1:
            row = '*'
        else:
            row = (row + ' ' + '*')
        i += 1
    print(row.center(new_length))
    stars += 1
print(new_string)
