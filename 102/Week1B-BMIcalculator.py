#   Austin Copley
#   ​CSCI 102 – Section B
#   Week 1 - Part B
lbs = float(input('WEIGHT> '))
inches = float(input('HEIGHT> '))
kg = lbs * 0.454
m = inches * 0.0254
bmi = kg / (m ** 2)
print('OUTPUT', round(bmi, 1))
