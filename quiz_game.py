print("welcome to my computer quiz! I Hope You Will Like This Quiz Game")

playing = input("Do you want to play the game?")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who won the first FIFA world cup and when? ")
if answer.lower() == "urugay in 1930":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("which team has the most UCL trophy in football ")
if answer.lower() == "real madrid":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("who is the highest paid footballer of all time? ")
if answer.lower() == "neymar":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("who won the most ISL trophy in Indian Super League? ")
if answer.lower() == "mohan bagan super giant":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")