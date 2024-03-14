is_magician = False 
is_expert = True 

if is_magician and is_expert:
    print("you are a master magician")
elif is_magician and not is_expert:
    print('at least your\'e getting there')
elif not is_magician:
    print('you need magic powers')


print(True == 1) # true
print('' == 1) # false
print([] == 1) # false
print(10 == 10.0) # true
print([] == []) # true



age = input("What is your age?: ")

if int(age) < 18:
	print("Sorry, you are too young to drive this car. Powering off")
elif int(age) > 18:
	print("Powering On. Enjoy the ride!");
elif int(age) == 18:
	print("Congratulations on your first year of driving. Enjoy the ride!")

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.