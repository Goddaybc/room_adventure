#Welcome to room adventure, a program to help use #A visitors room


#Prompt to the visitor
print ("Welcome to my room\n")
name = input ("What is your name?(Yes/No) ")
room = input ("Do you want to come in? ")
room = room.capitalize()
#A while loop to check decision of visitor
while room != " ":
    if room == "No":
        print ("Awww 💔 so sad")
        print ("Goodbye!!")
        break
    elif room == "Yes":
        print("Welcome")
#Asking the direction of user at the door mat
        direction = input ("Choose where you want to go? [Front: Back: Right: Left: ")
        direction = direction.lower()
        if direction == "back":
            print ("You have gone out the room, WHY!! 😞😞")
            break
        elif direction == "front":
            print ("\nWelcome to my parlour\n")
            print ("\nBeautiful parlour well painted well for your taste")
            direction = input ("\nChoose where you want to go? [Front: Back: Right: Left: \n")
            if direction == "front":
                print ("\nPhew!! Wrong direction, you hit my TV and Broke it 😦 turn back")
            elif direction == "right":
                print ("\nYou kicked Grandma and she was rush to the hospital and died\n")
            elif direction == "left":
                print (f"\nYou can have your sit {name} Welcome again!!\n")
            elif direction == "back":
                print ("\nWeakling, lol 🤣🤣 scary site right?!!\n")
            else:
                print ("You got lost in a small room dummy!!, Shame!! 😂😂😂")
        elif direction == "right":
            print ("\nYou hit a wall and died 💔💔")
            break
#incase user navigate to the kitchen
        elif direction == "left":
            print ("\n You entered into another room\n")
            direction = input ("Do you want to continue? (Yes/No): ")
            direction = direction.lower()
            if direction == "yes":
                print ("\nYou entered my kitchen now 🙈🥣🍨🍧🥮🍴🍾🔪🥄\n")
                print ("See our menu for rice\n")
                food_menu = ["Jollof", "Fried", "Stew","Sauce"]
                for menu in food_menu:
                    print(menu)
                direction = input("\nChoose your from the menu list: ")
                direction = direction.lower()
                if direction == "jollof":
                    print ("\nWell cooked Nigerian jollof with chicken yummy!! like you will love it enjoy buddy!\n")
                elif direction == "fried":
                    print ("\nHere is your well garnish fried rice specially made for you\n")
                elif direction == "stew":
                    print ("\nSorry to inform you there is no beef on the stew\n")
                    no_beef = input ("Will you take it like that?: (Yes/No) ")
                    no_beef = no_beef.lower()
                    if no_beef == "yes":
                        print ("Awww!! such a gentle man\n")
                    else:
                        print ("\nChoose another type of rice from menu list\n")
                elif direction == "sauce":
                    print ("\nSorry to inform you we don't have sauce available right now\n")
            else:
                print ("\nScary and lazy you bye!!\n")
                break
                    
