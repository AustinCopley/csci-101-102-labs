    #   Austin Copley
    #   ​CSCI 102 – Section B
    #   Week 2 - Lab - ReceiptGenerator
company = input("COMPANY> ")
streetaddress = input("STREET ADDRESS> ")
city_state_zip = input("CITY, STATE, ZIP> ")
cashier = input("CASHIER> ")
message = input("MESSAGE> ")
item1 = input("ITEM1> ")
price1 = float(input("PRICE1> "))
item2 = input("ITEM2> ")
price2 = float(input("PRICE2> "))
item3 = input("ITEM3> ")
price3 = float(input("PRICE3> "))
total = round(price1+price2+price3, 2)
print("            RECEIPT GENERATOR")
print("    ===================================")
print("        " + company)
print("        " + streetaddress)
print("        " + city_state_zip)
print("    ***********************************")
print("        Your cashier was: " + cashier )
print("        Welcome Valued Customer")
print("    ***********************************")
print("        Item Name       Item Price")
print(" ")
print("        " + str(item1) + "        " + str(price1))
print("        " + str(item2) + "        " + str(price2))
print("        " + str(item3) + "        " + str(price3))
print(" ")
print("    ***********************************")
print("        Total Cost of Order: " + str(total))
print("    ***********************************")
print("        " + message)
print("    ===================================")
