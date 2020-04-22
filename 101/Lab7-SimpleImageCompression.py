        #   Austin Copley
        #   CSCI 101 – Section F
        #   Python Lab 7

delim = ''

#START
start = 1
while start:

#MENU
    print("Simple Image Compression:")
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Enter an option:")
    print("1. Encode Image")
    print("2. Decode Image")
    print("3. Display Image")
    print("4. Quit")

    choice = int(input("OPTION> "))
    print('')

#ENCODE
    if choice == 1:
        print("OPTION 1: ENCODE IMAGE")
        string = list(input("ORIGINAL-STR> "))
        if '0' in string or '1' in string or '2' in string or '3' in string or '4' in string or '5' in string or '6' in string or '7' in string or '8' in string or '9' in string:
            valid = 0
            print("Number compression not supported")
            print("OUTPUT ERROR")
        else:
            valid = 1
        length = len(string)
        i = 0
        count = 1
        encoded_list = []
        
        while i < length and valid:
            if i == 0:
                count = 0
                letter = string[i]
            if letter == string[i]:
                count += 1
            if i == length - 1:
                encoded_list.append(str(count))
                encoded_list.append(string[i])
                count = 1
            if letter != string[i]:
                encoded_list.append(str(count))
                encoded_list.append(string[i - 1])
                count = 1
            if i < length - 1:
                letter = string[i]
            i += 1
            
        if valid:
            print("OUTPUT", delim.join(encoded_list))

        
#DECODE
    elif choice == 2:
        print("OPTION 2: DECODE IMAGE")
        encoded_string = input("ENCODED-STR> ")
        encoded_list = list(encoded_string)
        length = len(encoded_list)
        
        i = 0
        j = 0
        decoded_list = []
        
        while i < length:
            if (i + 1) % 2 == 1:
                mult = int(encoded_list[i])
            elif (i + 1) % 2 == 0:
                while j < mult:
                    decoded_list.append(encoded_list[i])
                    j += 1
            i += 1
            j = 0
                
        print("OUTPUT", delim.join(decoded_list))
        
    
#DISPLAY
    elif choice == 3:
        print("OPTION 3: DISPLAY IMAGE")
        image = input("IMAGE> ")
        row = int(input("ROW> "))
        column = int(input("COLUMN> "))

        i = 0
        c = 0
        r = 0
        line = []
        display = []
        
        while r < row:
            line = []
            while c < column:
                line.append(image[i])
                c += 1
                i += 1
            display.append(delim.join(line))
            print(delim.join(line))
            line = []
            r += 1
            c = 0
        print("OUTPUT", display)

#END
    elif choice == 4:
        print("OUTPUT Goodbye!")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        start = 0
        break


#INVALID INPUT
    else:
        print("ERROR: Please choose from [1-4]")
        print("OUTPUT ERROR")


#CONTINUE
    print("Would you like to continue (y/n)?")
    cont = input("CONTINUE> ").lower()
    if 'y' in cont:
        start = 1
        print('')
    elif 'n' in cont:
        print("OUTPUT Goodbye!")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
        start = 0
        break
