# JOberg_Assignment1_COP2373

# Define the parameters for each sale, return values to assigned variable
def sale(totaltickets):
    """
    Description:
    Asks for number of tickets to purchase, reduces from remaining

    Parameters:
    tsold (int): less than 4, < 4

    Variables:
    tsold (int): Number of tickets

    Logic:
    1. Ask for number of tickets to purchase
    2. Verify less than 4 tickets
        a. If less than 4 tickets, totaltickets - tsold
        b. If more than 4 tickets, return error

    Return:
    1. totaltickets
    2. tsold
    """
    tsold = int(input("How many tickets would you like to purchase? "))

    #If attempt to purchase more than 4 tickets, return error
    if tsold > 4:
        print("You cannot purchase more than 4 tickets")
        tsold = 0

    #Elif user attempts to purchase more tickets than remaining, return error
    elif tsold > totaltickets:
        print(f"{totaltickets} tickets remaining, cannot purchase.")
        tsold = 0

    #Else, tickets < 4 and totaltickets > 0, update total tickets remaining
    else:
        totaltickets -= tsold
        print(f"You purchased {tsold} tickets")
        print(f"There are {totaltickets} tickets remaining.")

    return totaltickets, tsold


def total(totaltickets):
    """
    Description:
    For all sales within tsold < 4 and totaltickets > 0, increase number of purchases (buyers)

    Parameters:
    totaltickets (int): starting number of tickets

    Variables:
    buyers (int): number of successful purchases

    Logic:
    1. While totaltickets > 0, loop
    2. Per transaction, increase number of purchases (buyers)

    Return:
    None
    """
    #First transcation purchasers = 0
    buyers = 0
    #While remaining tickets update sales
    while totaltickets > 0:
        totaltickets, tsold = sale(totaltickets)

        #Whhile non-error, increase purchasers
        if tsold > 0:
            buyers += 1
    print("There are no remaining tickets.")
    print(f"There were {buyers} buyers.")


def main():
    totaltickets = 20   # now lives inside a function
    total(totaltickets)


if __name__ == "__main__":
    main()
