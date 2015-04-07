 #introduction
print "You have just recieved a text from your inquiry class. "
print "Apparently, they are trapped in the lounge, which seems to be locked,from the outside by a passcode."
print "There are clues scattered around campus that will lead you to the password."
print "Find these clues and rescue your class!"
print "Your adventure starts at Togo Salmon Hall, otherwise known as TSH. "
print "You have the option of looking at your surroundings [look] or going [forward] to the MUSC food court"
location = 0

while True:	#location 0
	
	location_0_description = "You see a blue notebook lying on the ground. " \
	                         "It is covered in mud, and to be quite frank, quite gross looking." \
	                         " If you dare pick it up, type [look notebook]"

	object_1_description = "You open the notebook, and to your surprise you find that" \
	                       " it only has one letter written in it: T ." \
	                       "This HAS to mean something, someone must have left it there as a clue!"

	while location == 0:
		user_input = raw_input("What would you like to do? ")
		if user_input == "look":
			print location_0_description
		elif user_input == "look notebook":
			print object_1_description
		elif user_input == "forward":
			location = 1
		else:
			print "That is not a valid command."



	#location 1

	location_1_description ="As you walk into MUSC, the smell of food immediately draws you to the food court."\
	                        " You are just about to buy a slice of pizza when that little voice inside your head reminds "\
	                        "you that this is not the time to eat."\
	                        " Crestfallen, you decide to spend your time looking for clues instead. " \
	                        "After thoroughly searching you discover a bag of chips with the words 'open me' written on it and you also find a bookmark." \
	                        " Which of these objects would you like to examine first? Type [look chip bag] or [look bookmark] to examine either object." \
	                        "You also have to option to turn [right] and go to starbucks or go [forward] to Mills"
	object_2_description = "You open the chip bag. Inside you find a single chip shaped like a letter L. How odd!"
	object_3_description = "You examine the bookmark, it must be from the library because the letters HSL " \
	                      "are neatly printed on it. However, the letter H seems to have been circled by a red pen."


	if location == 1:
		print ("You are now in MUSC!")


	while location == 1:
		user_input = raw_input("What would you like to do? ")
		if user_input == "look":
			print location_1_description
		elif user_input == "look chip bag":
			print object_2_description
		elif user_input == "look bookmark":
			print object_3_description
		elif user_input == "right":
			location = 3
		elif user_input == "forward":
			location = 2
		else:
			print "That is not a valid command."


	#location 3
	location_3_description = "You pass by Starbucks, and although you try to keep walking," \
	                         " the temptation is too strong, and you find yourself lining up" \
	                         " for a cup of coffee. To look at the menu type [look menu]" \
	                        " you can also head outside by typing [forward]"
	object_4_description = "You look at the menu. You are about to order a Caramel Macchiato" \
	                        " when you notice that the name printed on the menu is missing an H." \
	                        " You make note of this observation"

	if location == 3:
		print ("You are now in the MUSC lobby near Starbucks!")



	while location == 3:
		user_input = raw_input("What would you like to do? ")
		if user_input == "look":
			print location_3_description
		elif user_input == "look menu":
			print object_4_description
		elif user_input == "forward":
			location = 4
		else:
			print "That is not a valid command."

	location_2_description = "You find yourself in the first floor of Mills Library. The sign for the library catches your eye. The librarian also looks eager to help. The exit outdoors is behind you and the door to the MUSC food court is to your left."
	if location == 2:
		print location_2_description

	sign_description = "the sign says \"Mills Memorial Library\". The \"Y\" seems particularly important to you, but you're not sure why. Haha, get it?"

	librarian = "Hi, are you looking for a book? "
	book_q2_answer = "I\'m afraid our current collection only includes Animorphs and Twilight. Which would you like? "
	animorphs_answer = "Oh, actually, it looks like we're all out of Animorphs, sorry!"


	while location == 2:
		user_input = raw_input("What would you like to do? ")
		if user_input == "look":
			print location_2_description
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
			location = 1
		elif user_input == "back":
			location = 4
			print "You are now outside."
		else:
			print "That is not a valid command."

	location_4_description = "You are standing outside of MUSC. The Willy Dog stand stands out to you. Haha, get it? You see The Starbucks is to your right, Mills Library is behind you, and MDCL lies to the left."

	Willy_Dog = "It\'s an endearing hot dog stand in the shape of a hot dog. The words 'Willy Dog' are written in red alongside a dog with a hot dog for a body. The 'W' in 'Willy' sticks out to you. The attendant looks friendly."

	Attendant_dialogue = "The girl attending the stand smiles as she asks, "

	if location == 4:
		print "You are now outside."
	while location == 4:
		user_input = raw_input("What would you like to do? ")
		if user_input == "look":
			print location_4_description
		elif user_input.lower() == "look willy dog" or user_input.lower() == "look willy" or user_input.lower() == "look willy dog stand":
			print Willy_Dog
		elif user_input == "talk" or user_input == "talk attendant":
			print Attendant_dialogue
			hotdog_choice = raw_input("\"Would you like a Willy Dog? Yes or no?\" ")
			if hotdog_choice.lower() == "yes":
				print "You suddenly remember that you're vegetarian and get a little bummed out."
			elif hotdog_choice.lower() == "no":
				print "You decline and pat yourself on the back for yet another successful social interaction."
			else:
				print "Everyone is a slightly weirded out by what you just said. Like seriously, why did you think that was even an option given the social context of the situation?"
		elif user_input == "right":
			location = 3
		elif user_input == "left":
			location = 6
		elif user_input == "back":
			location = 2
		elif user_input == "forward":
			print "You have trouble going up the stairs and give up."
		else:
			print "That is not a valid command."

	location_6_description = "You find yourself inside of MDCL. Behind you lies the Outdoors, and ahead of you is HSC. You wonder what Tim Horton\'s has on their menu today. You also happen to see one of your good friends at the cashier with a large cup of coffee in hand."
	if location == 6:
		print "You are inside MDCL."

	menu_description = "The menu reads Coffee : $1.60 (Medium) ; Donut : $0.99 ; Muffin : $1.29 ; Cookie : $0.99 ; 10-pack Timbits : $2.30 ; Cheesy Pizza : $5.00 ; Mac and Cheese : $4.00 (Large)."

	friend = "Hey! Haven't seen you in a while. Say...which course do you think is more stressful: Cell Bio or Inquiry?"
	cellbio_answer = "Yeah, Cell Bio's got me bogged down too. And the number of group meetings my group schedules each week is pretty crazy. I hardly have time for anything else!"
	inquiry_answer = "Heh, I suppose having the word \"Why\" thrown at you every class can be pretty stressful. Haha. Instantly, an image of the letter \"Y\" enters your mind, but you really aren't sure why."

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
			elif course_q1.lower() == "inquiry":
				print inquiry_answer
			else:
				print "Your friend leans closer and says, \"Sorry, what was that?\""
		elif user_input == "back":
			location = 4
		elif user_input == "forward":
			location = 7
		else: 
			print "That is not a valid command."


	location_7_description = "You are now inside of the Health Sciences Centre...Home of the Health Scis! Behind you is MDCL, and to your right is the Health Sci Lounge. Walking up the main flight of stairs, you notice a new sign placed outside of the Health Sciences Libary. You also notice a peculiar man standing outside of the library entrance."

	sign_description = "The sign reads: April 8th, 3:00 - 5:00 pm --- Dr. P.K. Rangachari, Professor (Emeritus) of Medicine, will be discussing his philosophy of teaching and his strategies for engaging students. All are welcome to attend. Refreshments will be served. Hmm...the \"I\" at the end of Chari's name is kind of crooked, you notice."

	man = "The peculiar man sees you approach. Why hello there! I'm a new prof in the Department of Pharmacology and Toxicology. *At this, the prof glances down at the library sign.* Did you hear the news? Dr. P.K. Rangachari will be giving a talk, right here in the library. Will you be attending?"
	yes_answer = "I'm glad. It's nice to see that young people are actually interested in attending these sorts of events. What's that? You say that Dr.Rangachari is your Cellular Biology professor? My, what a lucky student! I had the pleasure of working with Dr.Rangachari myself once...together, we published an article discussing how low doses of ionizing radiation can prevent radiation-induced colonic epithelial hyporesponsiveness to muscarnic agonists and...You zone out as this new prof keeps talking. The way he pronounces the \"C\" in Chari's name is particularly amusing, though."
	no_answer = "WHAT?! Don't be ridiculous! You really must attend, I mean, it is Dr. RANGACHARI that is speaking. THE Dr. RANGACHARI! How dare you not even consider attending an event in which he, The GREAT RANGACHARI, will be speaking. This goes to show just how self-absorbed and narrow-minded the youth of today are...I am absolutely disgusted with the world. My, the world must be ending! Yes, that's it! The world is -- at this, you slowly start to back away. The way be pronounced the \"C\" in Chari's name was particularly amusing, though."
	if location == 7:
		print "You are now in HSC!"
	while location == 7:
		user_input = raw_input("What would you like to do? ")
		if user_input == "look":
			print location_7_description
		elif user_input == "look sign":
			print sign_description
		elif user_input == "talk" or user_input == "talk man":
			answer_q1 = raw_input(man)
			if answer_q1.lower() == "yes":
				print yes_answer
			elif answer_q1.lower() == "no":
				print no_answer
			else:
				print "I'm sorry, I'm a little hard of hearing. Could you repeat that please?"
		elif user_input == "back":
			location = 6
		elif user_input == "right":
			location = 8
		else:
			print "That is not a valid command."

	location_8_description = "You now stand in front of the Health Sci Lounge. Behind you is the HSC lobby. You try to unlock the lounge door using your Health Sci access card, as you've always done, but the door doesn't budge. You notice a note with tiny writing taped to the door. It reads: Well, brave voyageur, looks like you've finally reached the lounge. Did you notice any strange looking letters along the way? Unscramble those letters and enter in your final answer in the keypad below. Answer correctly, and you will gain access to the lounge. Answer incorrectly, and you will face certain death. It's really that simple."
	congrats_message = "You hear the reassuring sound of a lock clicking. Slowly, you pull the handle of the door...and it opens! CONGRATULATIONS! You made it to the lounge in one piece! Thanks for playing!"

	while location == 8:
		user_input = raw_input("Enter the secret passcode below. Do not use spaces.")
		if user_input.lower() == "hcihywylt":
			print congrats_message
			break
		elif user_input == "back":
			location = 7
		else:
			print "I'm sorry, but that is not the correct passcode. Please try again."
	break

raw_input("Press enter to accept the praise of your peers.")