# This was an exercise I did to practice if statements. It is functional and feel free to use it if you're curious

weight = input('Type your weight here: ')
measurement = input("(K)g or (L)bs: ")

if measurement.upper() == "L":
    print("Weight in kg:", float(weight) * .45)
    
elif measurement.upper() == "K":
    print("weight in lbs:", float(weight) / .45)
    
else:
    print('ERROR, try again')