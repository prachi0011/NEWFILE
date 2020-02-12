n = int(input('enter the number : '))
name = "PYTHON"
for i in range(0,n):
	for j in range(i):
		print(name[i-1],end="")
	print()