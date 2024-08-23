
#########################################################################

#print floyds triangle given just the amount of rows desired

#Example
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# etc
    
def floydsTriangle(rowAmount):
    number = 1
    for currentRow in range(1, rowAmount + 1):  # Start from 1 to rowAmount
        for _ in range(currentRow):  # Repeat currentRow times
            print(number, end=" ")
            number += 1
        print()  # Move to the next line after finishing a row

#floydsTriangle(4)