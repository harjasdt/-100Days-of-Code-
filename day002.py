print("Welcom to tip calculator.")
bill=int(input("what was the total bill?"))
per=int(input("what percentage of tip would you like to give? 10 ,12 pr 15?"))
no=int(input("How many people to split the bill?"))
tip=round(per/bill,2)


ans=(bill+tip*100)/no
print(f'Each person should pay: {ans}')
