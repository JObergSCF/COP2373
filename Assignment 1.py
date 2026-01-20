#JOberg_Assignment1_COP2373

totaltickets = 20
tsold = 0
buyers = 0

#Define the parameters for each sale, return values to assigned variable
def sale(totaltickets):
    tsold = int(input("How many tickets would you like to purchase? "))
    if tsold > 4:
        print("You cannot purchase more than 4 tickets")
        tsold = 0
    elif tsold > totaltickets:
        print(f"{totaltickets} remaining, cannot purchase.")
        tsold = 0
    else:
        totaltickets -= tsold
        print(f"You purchased {tsold} tickets")
        print(f"There are {totaltickets} tickets remaining.")

    return totaltickets, tsold

#Accumulator/Running total and amount of tickets left
#Update buyer total
#Update tickets remaining (totaltickets)
def total(totaltickets):
    buyers = 0
    while totaltickets > 0:
        totaltickets, tsold = sale(totaltickets)
        if tsold > 0:
            buyers += 1
    print("There are no remaining tickets.")
    print(f"There were {buyers} buyers.")

total(totaltickets)