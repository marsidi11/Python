import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

ol = input("Original Link: ")

def check(ol):
	while ol[0:8] != "https://":
		print("Invalid Link \nTry Again!")
		ol = input("Original Link: ")
	
	while "." not in ol:
		print("Invalid Link \nTry Again!")
		ol = input("Original Link: ")
check(ol)	


def short(): 
	random.shuffle(characters)

	ch0 = "mz.ly/"
	
	ch1 = characters[1]
	ch2 = characters[2]
	ch3 = characters[3]
	ch4 = characters[4]
	ch5 = characters[5]

	shortened = ch0 + ch1 + ch2 + ch3 + ch4 + ch5

	print("\n")
	
	for i in range(0, len(ol) + 5):
		print("-", end="")

	print("\n~ Link: " + ol)
	print("~ Shorten Link: " + shortened)

	for i in range(0, len(ol) + 5):
		print("-", end="")

	print("\n")

short()

another = input("Do you want to short another link? (Y/N): ")


while another == "y" or another == "Y":
	ol = input("Original Link: ")
	check(ol)
	short()
	another = input("Do you want to short another link? (Y/N): ")

if another == "N" or another == "n":
	print("Ok. Goodbye!")


input("\nPress ENTER to exit")