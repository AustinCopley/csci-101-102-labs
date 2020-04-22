        #   Austin Copley
        #   ​CSCI 101 – Section F
        #   Python Lab 6

#initialize variables
user_list = []
start = True

while start == True:
    print("Review Search & Sort: ")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Enter an option: ")
    print("1. Enter a new list")
    print("2. Deploy Binary Search")
    print("3. Deploy Selection Sort")
    print("4. Quit")
    choice = input("OPTION> ")
    print('')
    
#menu choice error
    if choice.isdigit() == True:
        choice = int(choice)
        
    else:
        print("ERROR:", choice, "is not a valid integer!")
        print("OUTPUT ERROR")
        
    if choice > 4:
        print("")
        print("OUTPUT ERROR")
        print("")
        
    elif choice < 1:
        print("")
        print("OUTPUT ERROR")
        print("")

#menu choice 1
    elif choice == 1:
        print("OPTION 1: ENTER A NEW LIST")
        print("How many items are in this list?")
        size = input("LIST-SIZE> ")
        list1 = []
        if size.isdigit() == True:
            size = int(size)
            for i in range(size):
                add = input(f"ITEM {i}> ")
                if add.isdigit == False or add.isalpha() == True:
                    print("ERROR:", add, "is not a valid integer!")
                    print("OUTPUT ERROR")
                    break
                list1.append(int(add))
                i += 1
        else:
            print("ERROR:", size, "is not a valid integer!")
            print("OUTPUT ERROR")
    sort = True
#check if list is sorted
    i = 1
    while i < len(list1) - 1:
        if list1[i] <= list1[i+1]:
            sort = True
        else:
            sort = False
            break
        i += 1

#menu choice 2
    if choice == 2:
        print("OPTION 2: BINARY SEARCH")
        print("Input List: ", list1)
        if sort == True:
            target = input("BINARY-SEARCH-TARGET> ")
            if target.isdigit() == True:
                target = int(target)
                valid = True
            else:
                print("ERROR:", target, "is not a valid integer!")
                print("OUTPUT ERROR")
                valid = False
#Perform binary search
            if valid == True:
                length = len(list1)
                mid = length // 2
                count = 1
                i_min = 0
                i_max = length - 1
                
                while target != int(list1[mid]):
                    if target > int(list1[mid]):
                        i_min = mid + 1
                    elif target < int(list1[mid]):
                        i_max = mid - 1
                    count += 1
                    mid = i_min + (i_max - i_min) // 2
                    if i_max == i_min:
                        break
                if target == int(list1[mid]):
                    print("Target value", target, "found at index", mid)
                    print("OUTPUT ", mid)
                else:
                    print("Target", target, "NOT found in list.")
                    print("OUTPUT NOTFOUND")
                    
                    
                
                print("Total number of comparisons:", count)
                print("OUTPUT ", count)
            
        elif sort == False:
            print("ERROR: List unsorted! Please select option (3) to sort the list.")
            print("OUTPUT ERROR")
        
#menu choice 3
    elif choice == 3:
        print("OPTION 3: SORT THE LIST")
        list1 = sorted(list1)
        print("OUTPUT", list1)
        
#menu choice 4
    elif choice == 4:
        print("OUTPUT Goodbye!")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        start == False
        break

#continue
    if 0 < choice < 4: 
        print("Would you like to continue (y/n)?")
        cont = input("CONTINUE> ").lower()
        
        if cont == "y" or cont == "yes":
            start == True
            print('')
        elif cont == "n" or cont == "no":
            start == False
            print("OUTPUT Goodbye!")
            print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
            break

    else:
        print("")
        print("OUTPUT ERROR")
        print("")
