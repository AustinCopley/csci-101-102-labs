    #   Austin Copley
    #   ​CSCI 102 – Section B
    #   Week 4B - PrimeFactorization
start = 1
while start == 1:
    print("Enter a positive integer to generate its Prime Factors:")
    integer = int(input("INPUT> "))
    n = integer
    i = 2
    factor = list()
    while i <= n:
        if n % i == 0:
            factor.append(str(i))
            factor.append("*")
            n = n / i
        else:
            i += 1
    factor.pop(-1)
    empty = ''
    print("The Prime Factors for the integer", integer, "are:")
    print("OUTPUT", empty.join(factor))
    print("Do you want to get Prime Factors for another input? (y/n)")
    cont = input("CONTINUE> ").lower()
    if cont == "yes" or cont == "y" or cont == "yep":
        start = 1
        print("-------------------------------------------------------------")
    elif cont == "no" or cont == "n" or cont == "nope":
        start = 0
        print("-------------------------------------------------------------")
        print("Goodbye!")
