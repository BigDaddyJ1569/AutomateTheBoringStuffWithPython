#This program says hello and asks a couple questions.
#Written 8/26/22

print('Hello world!')
print("Oh! I didn't see you there, what is your name?")
myName = input()
print("It's good to meet you, " + myName +". Who is your favorite Dune character?")
faveDune = input()
print("Nice! I like " + faveDune + " too! How old are you?")
myAge = input()
print("You will be " + str(int(myAge) + 1) + " in a year.\nNext, you can enter your favorite quote from Dune and I will tell you how many characters are in in.")
quoteDune = input()
print("Your Dune quote has " + str(int(len(quoteDune))) + " characters in it.")