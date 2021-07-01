from itertools import product

die_sides = [1, 2, 3, 4, 5, 6]

num_dice = 3

dice = []

for i in range (num_dice):
    dice.append (die_sides)

print ("\ndice =", dice)

combos = list (product (*dice))

print ("\ncombos =", combos, "\n")
print (len (combos), " total combinations")