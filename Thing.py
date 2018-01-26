pCount = input('Please enter the number of people coming:')
pDur = input('Please enter the number of days in your stay')
pDest = input('Please enter your primary destination: ')
prefBudget = input('Please enter your prefered budget: ')
maxBudget = input('Please enter your maximum budget: ')
minOvernightSpend = input('Please enter the minimum you will spend on a single night of travel, minimum £10')

while int(minOvernightSpend)<10:
    minOvernightSpend = input('Please enter a new minimum Overnight spend equal to or greater than 10')

foodMinTotal = 10*int(pCount)*int(pDur)
print ('Your total food budget will need to be at minimum ' + str(foodMinTotal))
overnightMinTotal = int(minOvernightSpend)*int(pCount)*int(pDur)
print ('Your total overnight budget will need to be at a minimum ' + str(overnightMinTotal))
print ('Your total minimum budget is ' + str(overnightMinTotal+foodMinTotal))
