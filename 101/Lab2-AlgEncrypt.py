        #   Austin Copley
        #  ​ CSCI 101 – Section F
        #   Python Lab 2
        
list1 = input("LIST1> ")
list2 = input("LIST2> ")
list3 = input("LIST3> ")
list4 = input("LIST4> ")
list5 = input("LIST5> ")

out1 = list1[-2] + list1[-1] + list1[0:-2]
out2 = list2[0:-1]
middle = int(len(list3) / 2)
out3 = list3[middle:]
out4 = list4[2] + list4[1] + list4[0] + list4[3:]

encl = int(len(list5)/2)
front = list5[0:encl]
end = list5[encl:]

print('OUTPUT ', front, out1 + out2 + out3 + out4, end)
