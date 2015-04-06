location_6_description = "You find yourself inside of MDCL. Behind you lies the Outdoors, and ahead of you is HSC. You wonder what Tim Horton\'s has on their menu today. You also happen to see one of your good friends at the cashier with a large cup of coffee in hand."
if location = 6:
	print location_6_description

menu_description = "The menu reads Coffee : $1.60 (Medium) ; Donut : $0.99 ; Muffin : $1.29 ; Cookie : $0.99 ; 10-pack Timbits : $2.30 ; Cheesy Pizza : $5.00 ; Mac and Cheese : $4.00 (Large)."

friend = "Hey! Haven't seen you in a while. Say...which course do you think is more stressful: Cell Bio or Inquiry?"
cellbio_answer = "Yeah, Cell Bio's got me bogged down too. And the number of group meetings my group schedules each week is pretty crazy. I hardly have time for anything else!"
inquiry_answer = "Heh, I suppose having the word \"Why\" thrown at you every class can be pretty stressful. Haha. Instantly, an image of the letter \"Y\" enters your mind, but you really aren't sure why."

location = 6
while location == 6:
	user_input = raw_input("What would you like to do? ")
	if user_input == "look":
		print location_6_description
	elif user_input == "look menu":
		print menu_description
	elif user_input == "talk" or user_input == "talk friend":
		course_q1 = raw_input(friend)
		if course_q1.lower() == "cell bio":
			print cellbio_answer
		elif course_q1.lower() == "inquiry"
			print inquiry_answer
		else:
			print "Your friend leans closer and says, \"Sorry, what was that?\""
	elif user_input == "back":
		location = 4
	elif user_input == "forward":
		location = 7
	else: 
		print "That is not a valid command."


raw_input("Press enter to exit.")


