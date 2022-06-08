import random

pcNum = random.randint(1,10)
tries = 5
win = False
play = True


while play == True:
  while tries > 0:
    humNum = input("Pick a number between 1 and 10: ")

    if(int(humNum) == pcNum):
      win = True
      print("You Win")
      print(f"You had {tries} tries left until you lost.")
      break
    elif int(humNum) > 10 or int(humNum) < 0:
      print("You can't pick this number bozo.")
    else:
      tries -=1
      print("Try Again")
      print(f"You have {tries} tries left.")
      
    
  if win == False:
    print("Game Over")
    print(f"The correct number was {pcNum}")
  
  again = input("Would you like to play again? Y/N: ")  
  if again == "Y":
    tries = 5
    pcNum = random.randint(1,10)
  elif again == "N":
    print("Goodbye")
    play = False