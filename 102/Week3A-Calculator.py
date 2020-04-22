    #   Austin Copley
    #   ​CSCI 102 – Section B
    #   Week 3A - Calculator
operand_one = 0.0
operand_two = 0.0
operand_one = float(input("FIRST> "))
operand_two = float(input("SECOND> "))

print("Choose an operation")
print("1 - addition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
operation = int(input("OPERATION> "))

if (operation == 1):
    print('SUM:')
    print("OUTPUT ", operand_one + operand_two)
elif (operation == 2):
    print('DIFFERENCE:')
    print("OUTPUT ", operand_one - operand_two)
elif (operation == 3):
    print('PRODUCT:')
    print("OUTPUT ", operand_one * operand_two)
elif (operation == 4):
    print('QUOTIENT: ')
    print("OUTPUT ", int(operand_one // operand_two))
    print('REMAINDER:')
    print("OUTPUT ", round((operand_one % operand_two), 2))
else:
    print("Invalid Input.")
