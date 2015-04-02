location_0_description = "Description of the location, including things to look at, people to talk to, and other locations to go to (and their directions)"
print location_0_description

location = 0
while location == 0:
	if raw_input("What would you like to do? ") == "look":
		print location_0_description
	#elif raw_input("What would you like to do? ") == "look":
		#print ""
	else:
		print "That is not a recognized command."

raw_input("Press Enter to exit.")



