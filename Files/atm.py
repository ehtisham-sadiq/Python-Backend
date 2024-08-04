# atm system
# 1. user pin
# 2. check balance
# 3. depost balance
# 4. withdraw balance
# 5. change pin
# 6. exit the program
import random
print("\t\t====Welcome to HBL ATM Machine====\n")
balance = 0
pincode = 0
print("\t\t====Main Menu====\n")
while True:
	user_input = int(input("""
		1.Enter 1 to create Pin Code\n
		2.Enter 2 to check Balance\n
		3.Enter 3 to Deposit Balance\n
		4.Enter 4 to withdraw Balance\n
		5.Enter 5 to change Pin Code\n
		6.Enter 6 to Terminate Program\n\n
		"""))
	if user_input ==1:
		pincode = random.randint(1000,10001)
		print(f"Your ATM Pin Code is {pincode}")
		print("Don't Forget Your Pin Code!")
		print("\t\t---------------------------")
	if user_input==2:
		pin = int(input("Please, Enter Your Pin Code : "))
		if pin==pincode:
			print(f"Your Current Balance is {balance}")
		else:
			print("Please, Enter valid Pin Code")
		print("\t\t---------------------------")
	if user_input ==3:
		pin = int(input("Please,Enter Your Pin Code : "))
		if pin==pincode:
			amount = float(input("Enter amount you want to deposit : "))
			balance = amount+balance
			print("You have successfully deposit your amount!")
		else:
			print("Please, Enter valid Pin Code")
		print("\t\t---------------------------")
	if user_input==4:
		pin = int(input("Please, Enter your Pin Code : "))
		if pin==pincode:
			add_amount = int(input("Enter amount you want to withdraw : "))
			if balance>add_amount:
				print(f"You have withdraw{add_amount} rupess!")
				balance = balance-add_amount
				print(f"Your remaining balance is : {balance}")
			if balance<add_amount:
				print("You have insufficient Balance!")
		else:
			print("Please, Enter valid Pin Code!")
		print("\t\t----------------------------")
	if user_input==5:
		pincode = random.randint(1000,10001)
		print(f"Your ATM Pin Code is {pincode}")
		print("Don't Forget Your Pin Code!")
		print("\t\t---------------------------")
	if user_input==6:
		break

print("Program Terminates!!!!")
