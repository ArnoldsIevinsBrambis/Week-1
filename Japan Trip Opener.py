print ("Welcome to JapanJourney, because your garbage and you deserve garbage software :)")
pCount = input('Please enter the number of people coming (Max 10, cos lets be honest you dont have any more friends than that.')
while int(pCount)>10:
    pCount= input("Please enter a number 10 or lower")
places = ["Tokyo", "Hiroshima", "Kyoto", "Sapporo"]
done1=False
while done1==False:
    placeChoice = input("Please enter your preferred destination, out of Tokyo, Hiroshima, Kyoto and Sapporo (Case-Sensitive)")
    if (placeChoice in places):
        print("You have terrible taste")
        done1=True
    else:
        print("That wasn't even a fucking option, learn to read")
pCount = input("How many days are you planning on staying")
