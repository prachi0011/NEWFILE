list = [x for x in range(2000,3201)]
new_list = [l for l in list if l%7==0]
actual_list = [a for a in new_list if a%5!=0]
for i in actual_list:
	print(i,end=',')