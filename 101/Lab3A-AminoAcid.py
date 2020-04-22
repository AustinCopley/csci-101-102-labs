    #   Austin Copley
    #  ​CSCI 101 – Section F
    #   Python Lab 3A
C = int(input("CARBON> "))
H = int(input("HYDROGEN> "))
N = int(input("NITROGEN> "))
O = int(input("OXYGEN> "))
S = int(input("SULFUR> "))
if C == 3 and H == 7 and N == 1 and O == 2 and S == 0:
    print("OUTPUT: C_3H_7N_1O_2S_0")
    print("OUTPUT: Alanine")
elif C == 6 and H == 14 and N == 4 and O == 2 and S == 0:
    print("OUTPUT: C_6H_14N_4O_2S_0")
    print("OUTPUT: Arginine")
elif C == 4 and H == 8 and N == 2 and O == 3 and S == 0:
    print("OUTPUT: C_4H_8N_2O_3S_0")
    print("OUTPUT: Asparagine")
elif C == 3 and H == 7 and N == 1 and O == 2 and S == 1:
    print("OUTPUT: C_3H_7N_1O_2S_1")
    print("OUTPUT: Cysteine")
elif C == 6 and H == 9 and N == 3 and O == 2 and S == 0:
    print("OUTPUT: C_6H_9N_3O_2S_0")
    print("OUTPUT: Histidine")
elif C == 5 and H == 10 and N == 2 and O == 3 and S == 0:
    print("OUTPUT: C_5H_10N_2O_3S_0")
    print("OUTPUT: Glutamine")
else:
    print("Invalid amino acid")
