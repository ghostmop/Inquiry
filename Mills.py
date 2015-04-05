location_5_description = "You find yourself in the first floor of Mills Library. The sign for the library catches your eye. The librarian also looks eager to help. The exit outdoors is behind you and the door to the MUSC food court is to your left."
print location_5_description

sign_description = "the sign says \"Mills Memorial Library\". The \"Y\" seems particularly important to you, but you're not sure why. Haha, get it?"

librarian = "Hi, are you looking for a book? "
book_q2_answer = "I\'m afraid our current collection only includes Animorphs and Twilight. Which would you like? "
animorphs_answer = "Oh, actually, it looks like we're all out of Animorphs, sorry!"

location = 5
while location == 5:
	user_input = raw_input("What would you like to do? ")
	if user_input == "look":
		print location_5_description
	elif user_input == "look sign":
		print sign_description
	elif user_input == "talk" or user_input == "talk librarian":
		book_q1 = raw_input(librarian)
		if book_q1.lower() == "yes":
			book_q2 = raw_input(book_q2_answer)
			if book_q2.lower() == "animorphs":
				print animorphs_answer
				book_q2_answer = "I\'m afraid our current collection only includes Twilight. Which would you like? "
				animorphs_answer = "Nope, we haven't received any more Animorphs since the last time you asked."
			elif book_q2.lower() == "twilight":
				print "The librarian hands you a copy of Twilight. You politely decline."
			else:
				print "The librarian looks at you funny and says \"I'm sorry, I didn't catch that.\" and goes back to reading."
		elif book_q1.lower() == "no":
			print "The librarian replies, \"Oh, okay. Well, if you ever need any books, they will be here! In this library.\""
		else:
			print "\"Huh?\""
	elif user_input == "left":
		location = 2
	elif user_input == "back":
		location = 4
	else:
		print "That is not a valid command."

while location != 1: #this part is for debugging
	raw_input("That's all for this module!")
	print "Location = %s" %location
	break

raw_input("Press Enter to exit.")



