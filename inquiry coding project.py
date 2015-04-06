#introduction
print "You have just recieved a text from your inquiry class. "
print "Apparently, they are trapped in the lounge, which seems to be locked,from the outside by a passcode."
print "There are clues scattered around campus that will lead you to the password."
print "Find these clues and rescue your class!"

#location 0
print "Your adventure starts at Togo Salmon Hall, otherwise known as TSH. "
print "You have the option of looking at your surroundings [look] or going [forward] to the MUSC food court"
location_0_description = "You see a blue notebook lying on the ground. " \
                         "It is covered in mud, and to be quite frank, quite gross looking." \
                         " If you dare pick it up, type [look notebook]"

object_1_description = "You open the notebook, and to your surprise you find that" \
                       " it only has one letter written in it: T ." \
                       "This HAS to mean something, someone must have left it there as a clue!"

location = 0
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
while location == 4:
	raw_input("You are now outside! ")


raw_input("Press Enter to exit.")