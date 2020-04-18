def MainPage():
    print("Welcome to your Bank Account....")
    print("What would you like to do today?")
    print("Press A for Withdrawals")
    print("Press B for Deposits")
    print("Press C to view Account Details")
    print("Press D for Loan Request Information")
    print("Press Q to Log Off")
    Choice = input("Please Enter Letter Now")
       
    if Choice == 'a':
        DoWithdrawals()
    elif Choice == 'b':
        DoDesposits()
    elif Choice == 'c':
        DoAccountDetails
    elif Choice == 'd':
        DoLoanInfo()
    elif Choice == 'q':
        DoLogOff()
    else:
        print("Please Enter Valid Letter...")



#print(EvanKelly)

def DoWithdrawals():
 EvanKelly = []
 EvanKelly.append("Evan Preston Kelly")
 balance = 100
 EvanKelly.append(balance)
 Withdrawal = int(input("How much would you like to Withdraw?"))
 if Withdrawal < balance:
    print("Withdrawal sucessful")
    balance= balance - Withdrawal
    print("Your balance is {}".format(balance))
    print(EvanKelly)
 elif Withdrawal < balance:
    print("Unsufficient Funds..please try again")
    Withdrawal = int(input("How much would you like to Withdraw?"))
 else:
    print("Please Enter a valid amount")

def DoDesposits():
    Deposit = int(input("How much would you like to deposit?"))
    balance = 100

    if Deposit > 1:
        balance = balance + Deposit
        print("Your new Balance is {}".format(balance))
    else:
        print("Please Enter Valid Amount")
        Deposit = int(input("How much would you like to deposit?"))
        
        



MainPage()
    


