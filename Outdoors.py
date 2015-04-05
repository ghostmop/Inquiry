location_4_description = "You are standing outside of MUSC. The Willy Dog stand stands out to you. Haha, get it? You see The Starbucks is to your right, Mills Library is behind you, and MDCL lies to the left."
print location_4_description

Willy_Dog = "It\'s an endearing hot dog stand in the shape of a hot dog. The words 'Willy Dog' are written in red alongside a dog with a hot dog for a body. The 'W' in 'Willy' sticks out to you. The attendant looks friendly."

Attendant_dialogue = "The girl attending the stand smiles as she asks, "

location = 4
while location == 4:
	user_input = raw_input("What would you like to do? ")
	if user_input == "look":
		print location_4_description
	elif user_input.lower() == "look willy dog" or user_input.lower() == "look willy" or user_input.lower() == "look willy dog stand":
		print Willy_Dog
	elif user_input == "talk" or user_input == "talk attendant":
		print Attendant_dialogue
		hotdog_choice = raw_input("\"Would you like a Willy Dog? Yes or no?\"")
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
		location = 5
	elif user_input == "forward":
		print "You have trouble going up the stairs and give up."
	else:
		print "That is not a valid command."

while location != 4:
	raw_input("That's it for this module!")
	print location #This is for debugging!
	break #Debugging

raw_input("Press Enter to exit.")
