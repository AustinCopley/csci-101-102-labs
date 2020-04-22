        #   Austin Copley
        #  ​ CSCI 101 – Section F
        #   Python Lab 10

def multiply(x, y, z):
    if x * y == z:
        print("True")
    else:
        print("False")
    
def bounds_checking(low, upp, length):
    if low < 0 or low > upp or (upp - low) > length:
        print("False")
    else:
        print("True")

def decimal_points(num):
    num = str(num)
    i = 0
    dec = 0
    while i < len(num):
        if num[i] == '.':
            dec += len(num[(i + 1):])
            break
        i += 1
    if dec == 3:
        print("True")
    else:
        print("False")

def list_sorted(list_1):
    sort = True
    i = 1
    while i < len(list_1):
        if list_1[i] >= list_1[i - 1] and sort == True:
            sort = True
        else:
            sort = False
            break
        i += 1
    if sort:
        print("True")
    else:
        print("False")

def reversed_list(list_1, list_2):
    reverse = True
    i = 0
    while i < len(list_1):
        if list_1[i] == list_2[-(i+1)] and reverse == True:
            reverse = True
        else:
            reverse = False
            break
        i += 1
    if reverse:
        print("True")
    else:
        print("False")

def num_ohs(x, list_1):
    i = 0
    ohs = 0
    list_1 = str(list_1)
    while i < len(list_1):
        if list_1[i].lower() == 'o':
            ohs += 1
        i += 1
    if ohs == x:
        print("True")
    else:
        print("False")

def check_cs(string):
    i = 0
    c = False
    cs = False
    while i < len(string):
        if string[i] == 'c':
            c = True
        if c == True and string[i] == 's':
            cs = True
        i += 1
    if cs:
        print("True")
    else:
        print("False")

