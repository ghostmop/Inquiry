location_0_description = "Description of the location, including things to look at, people to talk to, and other locations to go to (and their directions)"
print location_0_description

object_1_description = "Description of object 1"
print object_1_description

object_2_description = "Description of object 2"
print object_2_description

location = 0
while location == 0:
	if raw_input("What would you like to do? ") == "look":
		print location_0_description
	elif raw_input("What would you like to do? ") == "look object 1":
		print "object_1_description"
	elif raw_input("What would you like to do? ") == "look object 2":
		print "object_2_description"
	elif raw_input("What would you like to do? ") == "right":
		location =1
	else:
		print "That is not a recognized command."

while location == 1:
	raw_input("You are now in a new location! ")
raw_input("Press Enter to exit.")



