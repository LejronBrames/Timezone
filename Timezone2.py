from datetime import datetime
now = datetime.now()

h = now.hour
m = now.minute
s = now.second

print("Timezone abbreviations are as follows: Samoa Standard Time (SST), Hawaii Standard time (HST), Alaskan Standard Time (AKST), Pacific Standard time (PST), Mountain Standard Time (MST), Central Standard Time (CST), Eastern Standard Time (EST), Atlantic Standard Time (AST)")

x = str(input("Please input your timezone in abbreviated form: "))

if x == str("SST"):
	print("It is currently:", int(h) - 15,":",m,":",s)
	
elif x == str("HST"):
	print("It is currently:", int(h) - 14,":",m,":",s)

elif x == str("AKST"):
	print("It is currently:", int(h) - 13,":",m,":",s)
	
elif x == str("PST"):
	print("It is currently:", int(h) - 12,":",m,":",s)
	
elif x == str("MST"):
	pprint("It is currently:", int(h) - 11,":",m,":",s)

elif x == str("CST"):
	print("It is currently:", int(h) - 10,":",m,":",s)
	
elif x == str("EST"):
	print("It is currently:", int(h) - 9,":",m,":",s)
	
elif x == str("AST"):
	print("It is currently:", int(h) - 8,":",m,":",s)
	
else:
	print("You did not enter a valid Timezone!")
	

