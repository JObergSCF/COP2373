class BankAcct:
    #Define class
    def __init__(self, name, acct_num, amount, rate):
        #Initialize
        self.name = name
        self.acct_num = acct_num
        self.amount = amount
        self.rate = rate

    #Define deposit logic
    def deposit(self, amt):
        self.amount += amt

    #Define withdrawal logic
    def withdraw(self, amt):
        if amt <= self.amount:
            self.amount -= amt
        #Failsafe for people not wanting overdraft fees
        else:
            print("Not enough funds")

    #Rate for account
    def set_rate(self, new_rate):
        self.rate = new_rate

    #Get balance
    def get_balance(self):
        return self.amount

    #Define interest logic
    def calc_interest(self, days):
        interest = self.amount * self.rate * (days / 365)
        return interest

    #Return account summary string
    def __str__(self):
        return f"{self.name} | Acct: {self.acct_num} | Balance: ${self.amount:.2f}"


def test_account():
    #Initialize account for testing
    acct = BankAcct("Student", 431823, 10, 0.05)

    print(acct)

    acct.deposit(500)
    print("After deposit:", acct)

    acct.withdraw(200)
    print("After withdrawal:", acct)

    acct.set_rate(0.03)
    print("New rate .03%")

    interest = acct.calc_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    print("Final balance:", acct.get_balance())


if __name__ == "__main__":
    test_account()