location_7_description = "You are now inside of the Health Sciences Centre...Home of the Health Scis! Behind you is MDCL, and to your right is the Health Sci Lounge. Walking up the main flight of stairs, you notice a new sign placed outside of the Health Sciences Libary. You also notice a peculiar man standing outside of the library entrance."
print location_7_description

sign_description = "The sign reads: April 8th, 3:00 - 5:00 pm --- Dr. P.K. Rangachari, Professor (Emeritus) of Medicine, will be discussing his philosophy of teaching and his strategies for engaging students. All are welcome to attend. Refreshments will be served. Hmm...the \"I\" at the end of Chari's name is kind of crooked, you notice."

man = "The peculiar man sees you approach. Why hello there! I'm a new prof in the Department of Pharmacology and Toxicology. *At this, the prof glances down at the library sign.* Did you hear the news? Dr. P.K. Rangachari will be giving a talk, right here in the library. Will you be attending?"
yes_answer = "I'm glad. It's nice to see that young people are actually interested in attending these sorts of events. What's that? You say that Dr.Rangachari is your Cellular Biology professor? My, what a lucky student! I had the pleasure of working with Dr.Rangachari myself once...together, we published an article discussing how low doses of ionizing radiation can prevent radiation-induced colonic epithelial hyporesponsiveness to muscarnic agonists and...You zone out as this new prof keeps talking. The way he pronounces the \"C\" in Chari's name is particularly amusing, though."
no_answer = "WHAT?! Don't be ridiculous! You really must attend, I mean, it is Dr. RANGACHARI that is speaking. THE Dr. RANGACHARI! How dare you not even consider attending an event in which he, The GREAT RANGACHARI, will be speaking. This goes to show just how self-absorbed and narrow-minded the youth of today are...I am absolutely disgusted with the world. My, the world must be ending! Yes, that's it! The world is -- at this, you slowly start to back away. The way be pronounced the \"C\" in Chari's name was particularly amusing, though."



location = 7
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

raw_input("Press enter to exit.")


