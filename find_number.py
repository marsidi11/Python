#Guess Number from 1 to 100!

from random import randint
# Start and End
first = 1
last = 100
number = randint(first, last)

#print(number)
print("Try to find the number between", first, "and", last)

x = None

while x != number:
	num = int(input("Number: "))
	x = int(num)

	if x < number:
		print("Higer!")
	elif:
		print("Lower!")

while x == number:
	print("Congratulation! You found the number. ")

	break

def exit():
	exit = input("Press ENTER to exit: ")

exit()