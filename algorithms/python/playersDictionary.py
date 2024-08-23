
#########################################################################
#Given a dictionary of username and status: ["online", "offline"]
#Return the number of players that are online

#Ex. 
players = {
    "Kira": "online",
    "bob": "offline",
    "wax": "online",
    "joe": "online"
}
#output => 3

def getplayercount(playerdict):
    count = 0
    for name, status in playerdict.items():
        if status == "online":
            count += 1
        
    
    return count
    
#print(getplayercount(players))