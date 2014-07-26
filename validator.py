cardnumber = raw_input("Type your Kian and Bruce ID card number, then press Enter. ")
def validatecard(cardnumber):
	if(cardnumber == "2243529956"):
		print("Validated successfully as:\
		Kian Moretz     \
		Co-Owner")
	elif(cardnumber == "1427184682"):
		print("Validated successfully as:\
		Bruce Kinzer    \
		Co-Owner")
	elif(cardnumber == "1250967843"):
		print("Validated successfully as:\
		Max             \
		Guard Dog")
	elif(cardnumber == "6627750914"):
		print("Validated successfully as:\
		Jonathan Moretz \
		Janitor")
	elif(cardnumber == "7865409143"):
		print("Validated successfully as:\
		Amanda Kinzer   \
		Accountant")
	elif(cardnumber == "6109975623"):
		print("Validated successfully as:\
		Jeremy Van Meter\
		Security Coordinator\
		Security Guard")
	elif(cardnumber == "5561232098"):
		print("Validated successfully as:\
		Anna Kinzer     \
		Receptionist")
	elif(cardnumber == "9056732218"):
		print("Validated successfully as:\
		Debbie Kinzer   \
		Document Reviewer")
	else:
		print("Invalid card number. Try again, please tell your validator.")

validatecard(cardnumber)