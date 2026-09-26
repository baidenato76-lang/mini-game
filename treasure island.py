print("welcome to treasure island.")
print("your mission is to find the treasure")


cross_road = input("youre at a cross road. Were do you want to go?  type 'left' or 'right'")

if cross_road == "left":
    river = input("you see a river.... 'swim' or 'wait'")
    if river == "wait":
        print("you waited and got across by boat safely")
        print("you enter a castle")
        castle_door = input("you come across a blue, red and yellow door...which door? ")
        if castle_door == "yellow":
            print("you see the princess... you win!!")
        elif castle_door == "red":
            print("room full of snakes... you lose")
        else:
            print("lava filled room... you got burnt to a crisp")
    else:
        print("you swam and got attacked by a crocodile... game over")
else:
    print(" the right road had lions... game over")