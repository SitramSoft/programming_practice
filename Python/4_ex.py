my_name = 'Zed A. Saw'
my_age = 35 			# not a lie
my_height = 74 			# inches
my_weight = 180 		# lbs
my_eyes = 'Blue'
my_teeth = 'Withe'
my_hair = 'Brown'

print("Let's talk about %s" % my_name)
print("He's %d inches or %d centimeters tall." % (my_height, my_height/0.3937))
print("He's %d pounds heavy." %my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(my_eyes, my_hair))
print("His teeth are usualy %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_weight + my_height))
