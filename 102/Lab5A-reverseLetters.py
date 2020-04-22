        #   Austin Copley
        #   ​CSCI 102 – Section B
        #   Week 5A - Reverse Only Letters

start = 1
while start == 1:
    print("Enter a string with letters to reverse.")
    string = input("STRING> ")
    stringList = list(string)
    blankList = []
    length = len(stringList)
    i = 1
    while i <= length:
        blankList.append('')
        i += 1
    
    i = 1
    index = 0
    
    while i <= length:
        if stringList[index].isalpha() == True:
            blankList[-i] = stringList[index]
        i += 1
        index +=1

    empty = ''
    temp_length = len(blankList)
    index = 0
    
    while index <= temp_length:
        if empty in blankList:
            blankList.remove(empty)
        index = index + 1
        
    index = 0
    
    while  index  < length:
        if stringList[index].isalpha() == False:
            blankList.insert(index, (stringList[index]))
        index +=1
    
    print("OUTPUT", empty.join(blankList))
    print("Do you want to reverse another string? (y/n)")
    cont = input().lower()
    if cont == "yes" or cont == "y" or cont == "yep":
        start = 1
        print("-------------------------------------------------------------")
        print("")
    elif cont == "no" or cont == "n" or cont == "nope":
        start = 0
        print("-------------------------------------------------------------")
        print("")
        print("Goodbye!")
    else:
        start = 0
        print("-------------------------------------------------------------")
        print("")
        print("Goodbye!")
