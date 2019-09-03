import pyperclip

def amazon():

	original_link = input("Amazon Product Link: ")

	original_link = original_link.split("dp/")[1]

	asin = original_link[:10]

	print("\n ** Amazon Product: https://www.amazon.com/dp/" + asin + "/")

	print(" ** ASIN Code: " + asin + " (Copied to Clipboard)" + "\n")

	pyperclip.copy(asin)

	amazon()

amazon()