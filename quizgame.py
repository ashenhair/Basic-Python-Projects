print("Welcome to my physics quiz!")

playing = input("Are you ready?: ")

if playing.lower() != "yes":
    quit()

print("Let's start!")
score = 0

question = input("Does a photon have mass?: ")

if question =="no":
    print("correct")
    score += 1
else:
    print("incorrect")

question = input("Which is the weakest force in nature?: ")

if question =="gravity":
    print("correct")
    score +=1
else:
    print("incorrect")

question = input("Is velocity scalar or vector?: ")

if question != "vector":
    print("incorrect")
else:
    print("correct")
    score +=1

#print(f"score değeri {score}")
print("You've got" + " " + str(score) + " "+"questions correct")
print("You've got" + " " + str((score/3)*100) + " " + "%")
    






