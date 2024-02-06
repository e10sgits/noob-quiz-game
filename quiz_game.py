print("Welcome to a computer quiz!")

playing = input("Do you want to participate? ")

if playing.lower() != "no":
    print("Okay! Let's play :) ")
    score = 0
    answer = input("What does CPU stand for? ")
else:
    playing = input("Are you sure yes or no? ")
    
    if playing.lower() != "no":
       quit()

if answer.lower() == "central processing unit": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower()== "random access memory": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got a " + str((score/4) * 100) + " %!")
print("Thank you for participating!")

playing = input("Would you like to try again? ")

if playing.lower() != "no":
    print("Okay! Let's play :) ")
    score = 0
    answer = input("What does CPU stand for? ")
else:
    playing = input("Are you sure yes or no? ")
    
    if playing.lower() != "no":
       quit()

if answer.lower() == "central processing unit": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower()== "random access memory": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply": 
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got a " + str((score/4) * 100) + " %!")
print("Thank you for participating!")



