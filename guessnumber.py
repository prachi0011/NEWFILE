print("Lets play a game , #######GUESSING A NUMBER #######")
s = input("enter START to play:  ")
print("guess a number from 1 to 10")
n = int(input("Guess a number:  "))
i = 0
s = 0
while i <= 10:
	if n == 5:
		s+=1

	else:
		print("WRONG GUESS")
		n = int(input("Again enter the number:  "))

		print(n)
	i+=1

if s > 0:
	print("HEY EXCELLENT YOU GUESS CORRECT")
print("end")
	
'''

I COMPLETED THE TASK


'''