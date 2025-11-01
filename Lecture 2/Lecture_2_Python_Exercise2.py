"""
Exercise - 2
ATM Machine menu
1. Pin change
2.balance check
3. withdraw
4. Deposit
5. Exit
"""

manu = input("""
Welcome to ATM Machine!
Please select an option:
1. Enter 1 for pin change.
2. Enter 2 for balance change.
3. Enter 3 for withdraw.
4. Enter 4 for deposit.
5. Enter 5 to exit.                                                                    
""")

if manu == "1":
    print("Pin change selected.")

elif manu == "2":
    print("Balance check selected.")

elif manu == "3":
    print("Withdraw selected.")

elif manu == "4":
    print("Deposit selected.")

elif manu == "5":
    print("Exit selected.")

else:
    print("Invalid option selected. Please try again.")        