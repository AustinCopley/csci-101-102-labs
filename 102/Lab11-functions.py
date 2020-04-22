#################################################
######## Austin Copley                       #########
######## Lab 11 - Function Definitions  #########
######## Section - B                               #########
#################################################

# Imports
import math

################################################
########   Function 1 : print_output   #########
################################################

def print_output(string):
    print("OUTPUT", string)

################################################
########   Function 2 : triangle_area  #########
################################################

def triangle_area(height, width):
    print_output(round(height * width / 2, 2))

################################################
########  Function 3 : feet_to_meters  #########
################################################

def feet_to_meters(feet):
    print_output(round(feet * 0.3048, 3))

################################################
########   Function 4 : polar_coords   #########
################################################

def polar_coords(x, y):
    print_output("r: " + str(round(math.sqrt( x * x + y * y ), 1)))
    print_output("theta: " + str(round(math.degrees(math.atan( y / x )), 1)))

################################################
######## Function 5 : is_prime         #########
################################################

def is_prime(num):
    i = 2
    prime = True
    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1
    if prime == False:
        print_output("False")
    elif prime == True:
        print_output("True")

################################################
######## Function 6 : euros_to_dollars #########
################################################

def euros_to_dollars(dollars):
    print_output(round((dollars * 1.08), 3))
