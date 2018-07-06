#!/usr/bin/python
def fruit_basket():
	basket_list = ["apple", "pear", "banana", "orange", "grape"]
	fruit = raw_input("Guess a fruit...\n")
	if (fruit) in basket_list:
		print ("Good guess!")
	else:
		print ("Nope")

fruit_basket()
