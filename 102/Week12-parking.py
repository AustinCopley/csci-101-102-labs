        #   Austin Copley
        #   CSCI 102 – Section B
        #   Week 12 - Parking Lot

import csv

def check_parking_lot(current_car, parking_lot, handicapped):
    
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if parking_lot == current_car and i < 2:
                parking_lot[i][j] = "EMPTY"
                return ("PARKING")
            elif parking_lot == current_car and i == 3:
                parking_lot[i][j] = "EMPTY"
                return ("HANDICAPPED")
            else:
                return (None)
            j += 1
        i += 1


def park_handicapped(current_car, handicapped):
    
    i = 0
    while i < 3:
        if handicapped[i] == "EMPTY":
            handicapped[i] = current_car
            break
        i += 1
    if "EMPTY" in handicapped:
        handicapped_full = False
    elif "EMPTY" not in handicapped:
        handicapped_full = True
    return handicapped_full


def park(current_car, parking_lot):

    check = False
    i = 0
    while i < 2:
        if check == True:
            break
        j = 0
        while j < 3:
            if parking_lot[i][j] == "EMPTY":
                parking_lot[i][j] = current_car
                check = True
                break
            j += 1
        i += 1
    parking_lot_full = True
    i = 0
    while i < 2:
        j = 0
        while j < 3:
            if parking_lot[i][j] == "EMPTY":
                parking_lot_full = False
                return (parking_lot_full)
            j += 1
        i += 1
        return (parking_lot_full)


def run():
    
    # parking_lot_full --> "Are there any open spots left in the parking lot?"
    parking_lot_full = False
    # handicapped_full --> "Are there any open handicapped spots left?"
    handicapped_full = False
    
    # parking_lot --> 2D list that contains the parking spot information
    parking_lot = []
    # parking_lot_size --> Integer representing the total parking spots
    parking_lot_size = 0
    
    # This with block fills parking_lot with the data from parking.csv
    with open('parking.csv', 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        for row in csvreader:
            parking_lot.append(row)
            parking_lot_size += len(row)
    
    # handicapped --> 1D list that contains the handicapped parking spot info
    handicapped = parking_lot[-1]
    
    # Your code here
    while parking_lot_full == False or handicapped_full == False:
        current_car = input("LICENSE PLATE> ")
        parking = check_parking_lot(current_car, parking_lot, handicapped)
        if parking == "PARKING":
            parking_lot_full = False
        elif parking == "HANDICAPPED":
            handicapped_full = False
        else:
            if current_car[0].isalpha() and current_car[0].lower() == 'h' and handicapped_full == False:
                handicapped_full = park_handicapped(current_car, handicapped)
            else:
                parking_lot_full = park(current_car, parking_lot)
    return (parking_lot)

    
    
###############################################################################


parking_lot = run()

print('!PARKING LOT FULL!')
print('!WRITING RESULTS TO output.csv!')
with open('output.csv', 'w', newline='') as f:
    w = csv.writer(f)
    for row in parking_lot:
        w.writerow(row)

