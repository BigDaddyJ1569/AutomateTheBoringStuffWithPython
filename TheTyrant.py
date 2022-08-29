# This program is here to showcase boolean logic in python
# Written 28/8/22

#this is the list that will hold the answers
answer = []
#this is the incremental for correct answers
aCorrect = 0
#this is the incremental for inncorect answers
aWrong = 0

print("Hello! Welcome to the Dune quote trivia game!\nDo you wish to play?")
if input() == "no":
    print("Well, that's no fun. Goodbye.")
    exit()
else:
    print("Awesome! Good luck, the game is about to begin!\n")

print("Question 1: What is the mind killer?\n")
answer.append(input())

if answer[0].title() ==  "Fear":
    print("Yes! Fear is the mind killer!")
    aCorrect += 1
else:
    print("No, that is incorrect. Fear is the mind killer.")
    aWrong += 1

print("\nQuestion 2: What clouds observation?")
answer.append(input())

if answer[1].title() == "Hope":
    print("Correct! Hope clouds observation")
    aCorrect += 1
else:
    print("No, that is incorrect. Hope is the answer we were looking for.")
    aWrong += 1

print("\nQuestion 3: The problem of __________ is inevitably: Who will play God?")
answer.append(input())

if answer[2].title() == "Leadership":
    print("Correct!")
    aCorrect += 1
else:
    print("No, that is incorrect. Leadership.")
    aWrong += 1
print("Let me tabulate your results...\n...\n...\n...\nOf the three questions asked, you got;\n" + str(int(aCorrect)) + " correct.\nAnd\n" + str(int(aWrong)) + " incorrect.\nThank you for playing!" )