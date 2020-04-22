        #   Austin Copley
        #   ​CSCI 101 – Section F
        #   Python Lab 5
start = 1
round_num = 0
while start == 1:
    print("Truth Table Generator | Round#", round_num)
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Enter an option:")
    print("1. OR Gate")
    print("2. AND Gate")
    print("3. XOR Gate")
    print("4. NOR Gate")
    print("5. NAND Gate")
    print("6. Quit")
    choice = int(input("OPTION> "))
    
    #       CHOICE 1
    if choice == 1:
        a, b = 0, 0
        if a == True or b == True:
            Q = 1
        else:
            Q = 0
        print("a b | OR")
        print("==========")
        print(a, b, "|", Q, "|")
        b += 1
        if a == True or b == True:
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        a += 1
        b = 0
        if a == True or b == True:
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        b += 1
        if a == True or b == True:
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        
        #       CHOICE 2
    elif choice == 2:
        a, b = 0, 0
        if a == True and b == True:
            Q = 1
        else:
            Q = 0
        print("a b | AND")
        print("==========")
        print(a, b, "|", Q, "|")
        b += 1
        if a == True and b == True:
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        a += 1
        b = 0
        if a == True and b == True:
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        b += 1
        if a == True and b == True:
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        
        #       CHOICE 3
    elif choice == 3:
        a, b = 0, 0
        if (a == True and  b == True) or (a == False and b == False):
            Q = 0
        elif (a == True and b == False) or (a == False and b == True):
            Q = 1
        print("a b | XOR")
        print("==========")
        print(a, b, "|", Q, "|")
        b += 1
        if (a == True and  b == True) or (a == False and b == False):
            Q = 0
        elif (a == True and b == False) or (a == False and b == True):
            Q = 1
        print(a, b, "|", Q, "|")
        a += 1
        b = 0
        if (a == True and  b == True) or (a == False and b == False):
            Q = 0
        elif (a == True and b == False) or (a == False and b == True):
            Q = 1
        print(a, b, "|", Q, "|")
        b += 1
        if (a == True and  b == True) or (a == False and b == False):
            Q = 0
        elif (a == True and b == False) or (a == False and b == True):
            Q = 1
        print(a, b, "|", Q, "|")
        
        #       CHOICE 4
    elif choice == 4:
        a, b = 0, 0
        if (not a == True) or (not b == True):
            Q = 1
        else:
            Q = 0
        print("a b | NOR")
        print("==========")
        print(a, b, "|", Q, "|")
        b += 1
        if (not a == True) or (not b == True):
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        a += 1
        b = 0
        if (not a == True) or (not b == True):
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        b += 1
        if (not a == True) or (not b == True):
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        
        #       CHOICE 5
    elif choice == 5:
        a, b = 0, 0
        if (not a == True) and (not b == True):
            Q = 1
        else:
            Q = 0
        print("a b | NAND")
        print("==========")
        print(a, b, "|", Q, "|")
        b += 1
        if (not a == True) and (not b == True):
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        a += 1
        b = 0
        if (not a == True) and (not b == True):
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")
        b += 1
        if (not a == True) and (not b == True):
            Q = 1
        else:
            Q = 0
        print(a, b, "|", Q, "|")

    elif choice == 6:
        start = 0
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("")
        print("Goodbye!")
        break
    round_num += 1
    cont = input("CONTINUE> ").lower()
    if cont == "yes" or cont == "y" or cont == "yep":
        start = 1
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("")
    elif cont == "no" or cont == "n" or cont == "nope":
        start = 0
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("")
        print("Goodbye!")
    else:
        start = 0
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        print("")
        print("Goodbye!")
