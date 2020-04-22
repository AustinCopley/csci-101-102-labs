    #   Austin Copley
    #   ​CSCI 101 – Section F
    #   Python Lab 4
print("Welcome to the Binary-Octal-Decimal Converter")
print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
start = 1
while start == 1:
    print("    Enter an option: ")
    print("1. Binary-Decimal Conversion")
    print("2. Decimal-Binary Conversion")
    print("3. Octal-Decimal Conversion")
    print("4. Decimal-Octal Conversion")
    print("5. Quit")
    choice = int(input("OPTION> "))

    
    if choice == 1:
        binary_str = input("BINARY-STR> ")
        binary_list = list(binary_str)
        i = -1
        power = 0
        dec = 0
        while (-i) <= len(binary_list):
            if int(binary_list[i]) > 1 or int(binary_str) < 0:
                print("ERROR: Input", binary_str, "is NOT a binary number.")
                dec = "ERROR"
                break;
            else:
                dec = dec + (int(binary_list[i]) * (2 ** power))
                power = power + 1
                i = i - 1
        print("OUTPUT", dec)

        
    elif choice == 2:
        decimal_str = input("DECIMAL-STR> ")
        binary = []
        j = 0
        n = 0
        a = ''
        if ('a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z') in list(decimal_str):
            print("ERROR: Input", decimal_str, "is NOT a decimal number.")
            binary = "ERROR"
            break;
            
        else:
            decimal = int(decimal_str)
            while n <= decimal:
                n = 2 ** (j + 1)
                m = 2 ** j
                decimal = int(decimal_str)
                if (decimal >= m):
                    binary.append('1')
                    decimal = decimal - m
                else:
                    binary.append('0')
                j = j + 1
        print("OUTPUT", a.join(binary))

        
    elif choice == 3:
        octal_str = input("OCTAL-STR> ")
        octal_list = list(octal_str)
        i = -1
        power = 0
        dec = 0
        while (-i) <= len(octal_list):
            if int(octal_list[i]) > 7 or int(octal_str) < 0:
                print("ERROR: Input", octal_str, "is NOT a octal number.")
                dec = "ERROR"
                break;
            else:
                dec = dec + (int(octal_list[i]) * (8 ** power))
                power = power + 1
                i = i - 1
        print("OUTPUT", dec)


    elif choice == 4:
        decimal_str = input("DECIMAL-STR> ")
        octal = []
        j = 0
        n = 0
        a = ''
        if ('a' or 'b' or 'c' or 'd' or 'e' or 'f' or 'g' or 'h' or 'i' or 'j' or 'k' or 'l' or 'm' or 'n' or 'o' or 'p' or 'q' or 'r' or 's' or 't' or 'u' or 'v' or 'w' or 'x' or 'y' or 'z') in list(decimal_str):
            print("ERROR: Input", decimal_str, "is NOT a decimal number.")
            octal = "ERROR"
            break;
            
        else:
            decimal = int(decimal_str)
            while n <= decimal:
                n = 8 ** (j + 1)
                decimal = int(decimal_str)
                if (n - decimal) == 0:
                    octal.append('1')
                else:
                    octal.append('0')
                j = j + 1
        print("OUTPUT", a.join(octal))

        
    elif choice == 5:
        start = 0
        print("OUTPUT Goodbye!")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    else:
        print("ERROR: Please choose from [1-5]")
        print("OUTPUT ERROR")
    print("Would you like to continue (y/n)?")
    cont = input("CONTINUE> ").lower()
    if cont == "yes" or cont == "y" or cont == "yep" or cont == "yes!":
        start = 1
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    elif cont == "no" or cont == "n" or cont == "nope" or cont == "no!":
        start = 0
        print("OUTPUT Goodbye!")
        print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
