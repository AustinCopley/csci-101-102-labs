        #Austin Copley
        #   ​CSCI 102 – Section B
        #   Week 8 - Part A

#get input
print("What size 2D list would you like to create?")
n = int(input("N> "))
print('')

                                #Solution 1
#initialize
i = 0
j = 1
k = 0
list_list = []
innerlist = []

#loop for list contents
while i < n:
    j = 1
    innerlist = []
    while j <= n:
        index = (i * n) + j
        innerlist.append(index)
        j += 1
    list_list.append(innerlist)
    i += 1

#loop for output
print("The original list is:")
print("[ ", end = '')
while k < n:
    if n - k != 1:
        print(list_list[k], end = '')
        print(", ")
    else:
        print(list_list[k])
    k += 1
print("]")
print('')

back_list = []
i = n - 1
while i >= 0:
    j = n
    innerlist = []
    while j > 0:
        index = (i * n) + j
        innerlist.append(index)
        j -= 1
    back_list.append(innerlist)
    i -= 1

#loop for output
k = 0
print("The reversed list is:")
print("[ ", end = '')
while k < n:
    if n - k != 1:
        print(back_list[k], end = '')
        print(", ")
    else:
        print(back_list[k])
    k += 1
print("]")
print('')


                                #Solution 2
#initialize
i = 0
j = 1
k = 0
list_list = []
innerlist = []

#loop for list contents
while i < n:
    j = 1
    innerlist = []
    while j <= n:
        index = (i * n) + j
        innerlist.append(index)
        j += 1
    list_list.append(innerlist)
    i += 1

#loop for output
print("The original list is:")
print("[ ", end = '')
while k < n:
    if n - k != 1:
        print(list_list[k], end = '')
        print(", ")
    else:
        print(list_list[k])
    k += 1
print("]")
print('')

#loop for reversed list
i = 0
list_list = []
while i < n:
    j = 1
    innerlist = []
    while j <= n:
        index = (i * n) + j
        innerlist.append(index)
        j += 1
    innerlist.reverse()
    list_list.append(innerlist)
    i += 1
list_list.reverse()

#loop for output
k = 0
print("The reversed list is:")
print("[ ", end = '')
while k < n:
    if n - k != 1:
        print(list_list[k], end = '')
        print(", ")
    else:
        print(list_list[k])
    k += 1
print("]")
