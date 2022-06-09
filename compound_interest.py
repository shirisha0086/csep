def compound_interest(principal,rate,year):
	if(year<=0):
		return principal
	else:
		return compound_interest(principal+principal*rate/100,rate,year-1)
print(compound_interest(1000,10,2))
