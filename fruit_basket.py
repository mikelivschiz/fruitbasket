#!/usr/bin/python

def fruit_basket(basket_list):
	myvar1 = 0
#	basket_list = ["jackfruit", "durian", "grapefruit", "pineapple", "banana"]
	while myvar1 < 5:
		fruit = raw_input("Guess a fruit...\n")
		if (fruit) in basket_list:
			print ("Good guess!")
			break
		else:
			myvar1 += 1
			if myvar1 == 5:
				print("You suck.  You lose.")
			else:
				print("That one is not in the basket.")
#fruit_basket()

def main():
	basket_list = ["jackfruit", "durian", "grapefruit", "pineapple", "banana"]
	fruit_basket(basket_list)

main()
