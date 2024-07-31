def main():
    # definition of variables
    xpn = False  # true if expansion active
    popFarm, popArt, popNew = [], [], []  # population cards
    obj1, obj2, obj3, obj4, obj5 = [], [], [], [], []  # points for objective cards
    gold = []  # amount of gold or points for gold
    end = []  # fireworks token, true if player triggers end of game
    xped = []  # expedition cards
    inno = []  # innovation cards
    airXplore = []  # exploration air ships
    airTrade = []  # trade air ships
    names = []  # list of player names

    # ask for player names
    names = [item for item in input("Please enter player names sepparated with only comma: ").split(",")]
    print("Welcome to the Scoreboard of Anno 1800: The Board Game!")
    
    # expansion active
    askXpn = input("Expansion active? (Y/N): ")
    askXpn = askXpn.upper()
    if askXpn == "Y":
        xpn = True
        #print("Expansion active.")
    elif askXpn == "N":
        xpn = False
        #print("Expansion not active.")
    else:
        print("Invalid input.")
        return
    print("")
        
    # ask for population cards
    for i in range(len(names)):
        askPopFarm = input("Please enter the number of FARMERS/WORKERS population cards for " + names[i].upper() + ": ")
        popFarm.insert(i, int(askPopFarm) * 3)
        askPopArt = input("Please enter the number of ARTISANTS/ENGINEERS/INVESTORS population cards for " + names[i].upper() + ": ")
        popArt.insert(i, int(askPopArt) * 8)
        askPopNew = input("Please enter the number of NEW WORLD population cards for " + names[i].upper() + ": ")
        popNew.insert(i, int(askPopNew) * 5)
        print("")
    #print(popFarm, popArt, popNew)
    print("")
    
    # ask for fireworks token
    askEnd = input("\nWho has the fireworks token? ")
    for i in range(len(names)):
        if names[i] == askEnd:
            end[:i] = [0] * i
            end[i+1:] = [0] * (len(names) - i - 1)
            end.insert(i, 7)
    #print(end)
    print("")
    
    #ask for objective cards
    askObj1Points = input("Do you get Influence Points for Objective Card 1? (Y/N): ")
    askObj1Points = askObj1Points.upper()
    if askObj1Points == "Y":
        for i in range(len(names)):
            askObj1 = input("Please enter Influence Points of Objective Card 1 for " + names[i].upper() + ": ")
            obj1.insert(i, int(askObj1))
        print("")
    
    askObj2Points = input("Do you get Influence Points for Objective Card 2? (Y/N): ")
    askObj2Points = askObj2Points.upper()
    if askObj2Points == "Y":
        for i in range(len(names)):
            askObj2 = input("Please enter Influence Points of Objective Card 2 for " + names[i].upper() + ": ")
            obj2.insert(i, int(askObj2))
        print("")
    
    askObj3Points = input("Do you get Influence Points for Objective Card 3? (Y/N): ")
    askObj3Points = askObj3Points.upper()
    if askObj3Points == "Y":
        for i in range(len(names)):
            askObj3 = input("Please enter Influence Points of Objective Card 3 for " + names[i].upper() + ": ")
            obj3.insert(i, int(askObj3))
        print("")
    
    askObj4Points = input("Do you get Influence Points for Objective Card 4? (Y/N): ")
    askObj4Points = askObj4Points.upper()
    if askObj4Points == "Y":
        for i in range(len(names)):
            askObj4 = input("Please enter Influence Points for Objective Card 4 for " + names[i].upper() + ": ")
            obj4.insert(i, int(askObj4))
        print("")
    
    askObj5Points = input("Do you get Influence Points for Objective Card 5? (Y/N): ")
    askObj5Points = askObj5Points.upper()
    if askObj5Points == "Y":
        for i in range(len(names)):
            askObj5 = input("Please enter Influence Points of Objective Card 5 for " + names[i].upper() + ": ")
            obj5.insert(i, int(askObj5))
            
    #print(obj1, obj2, obj3, obj4, obj5)
    print("")
        
    # ask for gold
    for i in range(len(names)):
        askGold = input("Please enter the amount of GOLD for " + names[i].upper() + ": ")
        gold.insert(i, int(askGold) // 3)
    #print(gold)
    print("")
    
    # ask for expedition cards
    for i in range(len(names)):
        askXped = input("Please enter Influence Points of EXPEDITION CARDS for " + names[i].upper() + ": ")
        xped.insert(i, int(askXped))
    #print(xped)
    print("")
    
    # don't ask for innovation cards and airships if expansion not active
    if xpn == True:
        # ask for innovation cards
        for i in range(len(names)):
            askInno = input("Please enter the number of INNOVATION cards for " + names[i].upper() + ": ")
            inno.insert(i, int(askInno) * 2)
        #print(inno)
        print("")
            
        # ask for air ships
        for i in range(len(names)):
            askAirX = input("Please enter the number of EXPLORATION AIR SHIPS for " + names[i].upper() + ": ")
            airXplore.insert(i, int(askAirX) * 4)
        #print(airXplore)
        print("")
        
        for i in range(len(names)):
            askAirT = input("Please enter the number of TRADING AIR SHIPS for " + names[i].upper() + ": ")
            airTrade.insert(i, int(askAirT) * 3)
        #print(airTrade)
        print("\n")
        
    # calculate total points for each player
    for i in range(len(names)):
        totalPoints = popArt[i] + popFarm[i] + popNew[i] + end[i] + (obj1[i] if bool(obj1) else 0) + (obj2[i] if bool(obj2) else 0) + (obj3[i] if bool(obj3) else 0) + (obj4[i] if bool(obj4) else 0) + (obj5[i] if bool(obj5) else 0)  + xped[i] + (inno[i] + airXplore[i] + airTrade[i] if xpn else 0)  + gold[i]
        print(names[i] + " has " + str(totalPoints) + " total points.\n")
        
if __name__ == "__main__":
    main()