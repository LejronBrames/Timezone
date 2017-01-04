from datetime import datetime
now = datetime.now()

print("Timezone abbreviations are as follows: Samoa Standard Time (SST), Hawaii Standard time (HST), Alaskan Standard Time (AKST), Pacific Standard time (PST), Mountain Standard Time (MST), Central Standard Time (CST), Eastern Standard Time (EST), Atlantic Standard Time (AST)")

x = str(input("Please input your timezone in abbreviated form: "))

if x == str("SST"):
	print("It is Currently:")
	print(int(now.hour) - 15, now.minute, now.second)

if x == str("HST"):
	print("It is Currently:")
	print(int(now.hour)) - 14 , now.minute , now.second 

if x == str("AKST"):
	print("It is Currently:")
	print(int(now.hour) - 13, now.minute, now.second)
	
if x == str("PST"):
	print("It is Currently:")
	print(int(now.hour) - 12, now.minute, now.second)

if x == str("MST"):
	print("It is Currently:")
	print(int(now.hour) - 11, now.minute, now.second)

if x == str("CST"):
	print("It is Currently:")
	print(int(now.hour) - 10, now.minute, now.second)
	
if x == str("EST"):
	print("It is Currently:")
	print(int(now.hour) - 9, now.minute, now.second)

if x == str("AST"):
	print("It is Currently:")
	print(int(now.hour) - 8, now.minute, now.second)
	
