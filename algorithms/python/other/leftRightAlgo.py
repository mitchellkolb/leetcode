 #########################################################################


#Given a list of sorted numbers determine if 2 unique numbers add up to 9
list = [1,2,3,4,5]

def addUpToNine(list):
    index = len(list) -1
    guess = 9 - list[index]
    if guess < list[index]:
        print(f"{guess} and {list[index]}")
    
addUpToNine(list)
