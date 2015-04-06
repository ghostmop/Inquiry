location_8_description = "You now stand in front of the Health Sci Lounge. Behind you is the HSC lobby. You try to unlock the lounge door using your Health Sci access card, as you've always done, but the door doesn't budge. You notice a note with tiny writing taped to the door. It reads: Well, brave voyageur, looks like you've finally reached the lounge. Did you notice any strange looking letters along the way? Unscramble those letters and enter in your final answer in the keypad below. Answer correctly, and you will gain access to the lounge. Answer incorrectly, and you will face certain death. It's really that simple."
print location_8_description

congrats_message = "You hear the reassuring sound of a lock clicking. Slowly, you pull the handle of the door...and it opens! CONGRATULATIONS! You made it to the lounge in one piece! Thanks for playing!"

location = 8
while location == 8:
	user_input = raw_input("Enter the secret passcode below. Do not use spaces.")
	if user_input == "HCIHYWYLT":
		print congrats_message
	elif user_input == "back":
		location = 7
	else:
		print "I'm sorry, but that is not the correct passcode. Please try again."

raw_input("Press enter to exit.")


	
