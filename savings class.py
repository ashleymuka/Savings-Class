'''
Description: develop a banking system to manage different types of accounnts
'''


class SavingsAccount:
    
    def __init__(self, account_number, interest_rate, balance):
        self.account_number = account_number
        self.interest_rate = interest_rate
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_account_details(self):
        return f"SavingsAccount\n-------------\nAccount number: {self.account_number}\nInterest rate: {self.interest_rate:.1f}%\nBalance: ${self.balance:,.2f}\n"
        

class CD(SavingsAccount):
    def __init__(self, account_number, interest_rate, balance, maturity_date):
        super().__init__(account_number, interest_rate, balance)
        self.maturity_date = maturity_date

    def get_maturity_date(self):
        return self.maturity_date

    def set_maturity_date(self, maturity_date):
        self.maturity_date = maturity_date

    def get_account_details(self):
        return f"CD\n-------------\nAccount number: {self.account_number}\nInterest rate:{self.interest_rate:.1f}%\nBalance: ${self.balance:,.2f}\nMaturity date: {self.maturity_date}\n"
        

if __name__ == "__main__":


    savings_acc = SavingsAccount("1234SA", 3.5, 1000)
    cd_acc = CD("2345CD", 5.6, 2500, "12/12/2023")

    print(savings_acc.get_account_details())
    print(cd_acc.get_account_details())

    balance = float(input("Enter your balance: \n"))
    interest_rate = float(input("Enter your interest rate: \n"))

    savings_acc2 = SavingsAccount("SA_No2", interest_rate, balance)
    cd_acc2 = CD("CD_No2", interest_rate, balance, "10/31/2023")

    print(savings_acc2.get_account_details())
    print(cd_acc2.get_account_details())












