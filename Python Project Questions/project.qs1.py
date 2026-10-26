balance=10000
correct_pin=1234
attempt=3
dep=0
wit=0
usr_pin=int(input(f"Enter your pin: "))
while usr_pin!=correct_pin:
    attempt-=1
    if attempt>0:
        print(f"Wrong Pin,{attempt} attempt left.")
        usr_pin=int(input("Enter your pin again: "))
    else:
        print("Card Blocked, Try again later.")
        break

while usr_pin==correct_pin:
    choise=input("\n1:Check Balance, \n2:Deposit, \n3:Withdraw, \n4:Exit \nEnter your choise:")
    if choise=="1":
        print("Your Balance is: ",balance)
    elif choise=="2":
        deposit=int(input("Enter your amount: "))
        print("Amount Deposit is Sucessful.")
        print("Your new balance is: ", balance+deposit)
        dep+= deposit
        balance+=deposit
    elif choise=="3":
        withdraw=int(input("Enter amount to withdraw: "))
        if withdraw>balance:
            print("Insufficient Balance.")
            continue
        print("Withdraw Amount Sucessful of:",withdraw )
        print("Your remaining amount is:",balance-withdraw)
        balance-=withdraw
        wit+=withdraw 
    elif choise=="4":
        print("Exited, \nThank you for using our Services.")
        print(f"Your History:\nYour Deposit: {deposit}.\nAmount withdrawn: {withdraw}")
        break

        
   
