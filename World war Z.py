from random import randint
import time

zombie_life=100
player_life=100
player_death=False
zombie_death=False

print("Welcome to the World War Z !!")
time.sleep(1.3)
print()
name=input("Enter your name here: ")
print()
print("Fight for your life and kill them all " + name + "!")
time.sleep(1.8)
print()
print("Game loading...10%")
time.sleep(1.9)
print("Game loading...23%")
time.sleep(1.7)
print("Game loading...69%")
time.sleep(2.1)
print("Game loading...99%")
time.sleep(2.9)
print("Game loading...100%")
time.sleep(.9)
print()
print("Game started!")
time.sleep(1)
print()
print("Your weapon: Gun, Knife, Punch")
time.sleep(1)
print()
player_turn=input(name + " what weapon do you want to use? ").lower()
print()
 
 
if player_turn == "punch" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
    print()
  print("You punch zombie in the head!")
  time.sleep(1)
  print("You have made 15 damage!")
  time.sleep(1)
  zombie_life-=15
  print("zombie remaining life: " + str(zombie_life) +"%")
  
elif player_turn=="knife" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You stab zombie in the head!")
  time.sleep(1.8)
  print("You dealth 20 damage!")
  time.sleep(1)
  zombie_life-=20
  print("zombie remaining life: " + str(zombie_life) + "%")
  
elif player_turn=="gun" and not(player_death):
  if zombie_life<=0: 
    print("You win!")  
    exit()    
    print()
  print("You shoot zombie in the head!")
  time.sleep(1.7)
  print("You dealt 25 damage!")
  time.sleep(1.3)
  zombie_life-=25
  print("zombie remaining life: " + str(zombie_life) + "%")
  
else:
  print("invalid attack, zombie missed!")

time.sleep(1.9)
print() 
print("zombie is thinking...")
time.sleep(3)
print()




zombie_choice=["bite","scratch", "acid"]
computer= zombie_choice [randint(0,2)]

print ("zombie used " + computer + "!")
time.sleep(1.2)
if computer=="bite" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie bite your arm!")
  time.sleep(1.3)
  print("zombie dealt 15 damage to you!")
  time.sleep(1.2)
  player_life-=15
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="acid" and not(zombie_death):
  if player_life<=0:
    exit()
    print("Zombie win!")
  print("zombie blast an acid to you!")
  time.sleep(1.4)
  print("zombie dealt 30 damage to you")
  time.sleep(1.2)
  player_life-=30
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="scratch" and not(zombie_death):
  if player_life<=0:
    exit()
    print("Zombie win!")
  print("zombie scratch your face!")
  time.sleep(1.2)
  print("zombie dealt 20 damage to you")
  time.sleep(1.2)
  player_life-=20
  print("Your remaining life: " + str(player_life) + "%")

time.sleep(1.2)
print()
print("Your weapon: Gun, Knife, Punch")
time.sleep(1)
print()



player_turn=input(name + " what weapon do you want to use? ").lower()
print()
if player_turn == "punch" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You punch zombie in the head!")
  time.sleep(1)
  print("You dealth 15 damage!")
  time.sleep(1)
  zombie_life-=15
  print("zombie remaining life: " + str(zombie_life) +"%")
  
elif player_turn=="knife" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You stab zombie in the head!")
  time.sleep(1.8)
  print("You dealth 20 damage!")
  time.sleep(1)
  zombie_life-=20
  print("zombie remaining life: " + str(zombie_life) + "%")
  
elif player_turn=="gun" and not(player_death):
  if zombie_life<=0: 
    print("You win!")   
    exit()   
    print()
  print("You shoot zombie in the head!")
  time.sleep(1.7)
  print("You dealt 25 damage!")
  time.sleep(1.3)
  zombie_life-=25
  print("zombie remaining life: " + str(zombie_life) + "%")
  
else:
  print("invalid attack, zombie missed!")

time.sleep(1.9)
print()
print("zombie is thinking...")
time.sleep(3)
print()




zombie_choice=["bite","scratch", "acid"]
computer= zombie_choice [randint(0,2)]

print ("zombie used " + computer + "!")
time.sleep(1.2)
if computer=="bite" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie bite your arm!")
  time.sleep(1.3)
  print("zombie dealt 15 damage to you!")
  time.sleep(1.2)
  player_life-=15
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="acid" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie blast an acid to you!")
  time.sleep(1.4)
  print("zombie dealt 30 damage to you")
  time.sleep(1.2)
  player_life-=30
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="scratch" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie scratch your face!")
  time.sleep(1.2)
  print("zombie dealt 20 damage to you")
  time.sleep(1.2)
  player_life-=20
  print("Your remaining life: " + str(player_life) + "%")
print()
time.sleep(1.2)
print()



print("Your weapon: Gun, Knife, Punch")
player_turn=input(name + " what weapon do you want to use? ").lower()
print()
if player_turn == "punch" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You punch zombie in the head!")
  time.sleep(1)
  print("You dealth 15 damage!")
  time.sleep(1)
  zombie_life-=15
  print("zombie remaining life: " + str(zombie_life) +"%")
  
elif player_turn=="knife" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You stab zombie in the head!")
  time.sleep(1.8)
  print("You dealth 20 damage!")
  time.sleep(1)
  zombie_life-=20
  print("zombie remaining life: " + str(zombie_life) + "%")
  
elif player_turn=="gun" and not(player_death):
  if zombie_life<=0: 
    print("You win!")      
    exit()
    print()
  print("You shoot zombie in the head!")
  time.sleep(1.7)
  print("You dealt 25 damage!")
  time.sleep(1.3)
  zombie_life-=25
  print("zombie remaining life: " + str(zombie_life) + "%")
  
else:
  print("invalid attack, zombie missed!")
print()
print("zombie is thinking...")

time.sleep(3)



zombie_choice=["bite","scratch", "acid"]
computer= zombie_choice [randint(0,2)]

print ("zombie used " + computer + "!")
time.sleep(1.2)
if computer=="bite" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie bite your arm!")
  time.sleep(1.3)
  print("zombie dealt 15 damage to you!")
  time.sleep(1.2)
  player_life-=15
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="acid" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie blast an acid to you!")
  time.sleep(1.4)
  print("zombie dealt 30 damage to you")
  time.sleep(1.2)
  player_life-=30
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="scratch" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie scratch your face!")
  time.sleep(1.2)
  print("zombie dealt 20 damage to you")
  time.sleep(1.2)
  player_life-=20
  print("Your remaining life: " + str(player_life) + "%")

time.sleep(1.2)
print()




print("Your weapon: Gun, Knife, Punch")
time.sleep(1)
print()
player_turn=input(name + " what weapon do you want to use? ").lower()
print()

if player_turn == "punch" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You punch zombie in the head!")
  time.sleep(1)
  print("You dealth 15 damage!")
  time.sleep(1)
  zombie_life-=15
  print("zombie remaining life: " + str(zombie_life) +"%")
  
elif player_turn=="knife" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You stab zombie in the head!")
  time.sleep(1.8)
  print("You dealth 20 damage!")
  time.sleep(1)
  zombie_life-=20
  print("zombie remaining life: " + str(zombie_life) + "%")
  
elif player_turn=="gun" and not(player_death):
  if zombie_life<=0: 
    print("You win!")      
    exit()
    print()
  print("You shoot zombie in the head!")
  time.sleep(1.7)
  print("You dealt 25 damage!")
  time.sleep(1.3)
  zombie_life-=25
  print("zombie remaining life: " + str(zombie_life) + "%")
  
else:
  print("invalid attack, zombie missed!")

time.sleep(1.9)
print()
print("zombie is thinking...")
time.sleep(3)
print()




zombie_choice=["bite","scratch", "acid"]
computer= zombie_choice [randint(0,2)]

print ("zombie used " + computer + "!")
time.sleep(1.2)
if computer=="bite" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie bite your arm!")
  time.sleep(1.3)
  print("zombie dealt 15 damage to you!")
  time.sleep(1.2)
  player_life-=15
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="acid" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie blast an acid to you!")
  time.sleep(1.4)
  print("zombie dealt 30 damage to you")
  time.sleep(1.2)
  player_life-=30
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="scratch" and not(zombie_death):
  print("zombie scratch your face!")
  time.sleep(1.2)
  print("zombie dealt 20 damage to you")
  time.sleep(1.2)
  player_life-=20
  if player_life<=0:
    print("You win!")
  print("Your remaining life: " + str(player_life) + "%")
print()
time.sleep(1.3)



print("Your weapon: Gun, Knife, Punch")
time.sleep(1)
print()
player_turn=input(name + " what weapon do you want to use? ").lower()
print()

if player_turn == "punch" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You punch zombie in the head!")
  time.sleep(1)
  print("You dealth 15 damage!")
  time.sleep(1)
  zombie_life-=15
  print("zombie remaining life: " + str(zombie_life) +"%")
  
elif player_turn=="knife" and not(player_death):
  if zombie_life<=0:
    print("You win!")
    exit()
  print()
  print("You stab zombie in the head!")
  time.sleep(1.8)
  print("You dealth 20 damage!")
  time.sleep(1)
  zombie_life-=20
  print("zombie remaining life: " + str(zombie_life) + "%")
  
elif player_turn=="gun" and not(player_death):
  if zombie_life<=0: 
    print("You win!")  
    exit()    
    print()
  print("You shoot zombie in the head!")
  time.sleep(1.7)
  print("You dealt 25 damage!")
  time.sleep(1.3)
  zombie_life-=25
  print("zombie remaining life: " + str(zombie_life) + "%")
  
else:
  print("invalid attack, zombie missed!")

time.sleep(1.9)
print()
print("zombie is thinking...")
time.sleep(3)
print()




zombie_choice=["bite","scratch", "acid"]
computer= zombie_choice [randint(0,2)]

print ("zombie used " + computer + "!")
time.sleep(1.2)
if computer=="bite" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie bite your arm!")
  time.sleep(1.3)
  print("zombie dealt 15 damage to you!")
  time.sleep(1.2)
  player_life-=15
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="acid" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie blast an acid to you!")
  time.sleep(1.4)
  print("zombie dealt 30 damage to you")
  time.sleep(1.2)
  player_life-=30
  print("Your remaining life: " + str(player_life) + "%")
  
elif computer=="scratch" and not(zombie_death):
  if player_life<=0:
    print("Zombie win!")
    exit()
  print("zombie scratch your face!")
  time.sleep(1.2)
  print("zombie dealt 20 damage to you")
  time.sleep(1.2)
  player_life-=20
  print("Your remaining life: " + str(player_life) + "%")
if zombie_death:
  print("You win")
else:
  print("Zombie win .Sad would you like to play again.")