location_0_description = "Description of the location, including things to look at, people to talk to, and other locations to go to (and their directions)"
print location_0_description

location = 0
while location == 0:
	user_input = raw_input("What would you like to do? ")
	if user_input == "look":
		print location_0_description
	elif user_input == "look object1":
		print "object 1 description"
	elif user_input == "right":
		location = 1
	else:
		print "That is not a valid command."
while location == 1:
	raw_input("You are now in a new location! ")
raw_input("Press Enter to exit.")



