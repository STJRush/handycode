#simple sort

"""
Start with a list
"""
unsortedlisty = [5,4,1,51,87,56,23,32]

"""
Make an empty list
"""

sortedlisty = []

meLENT = len(unsortedlisty)
print("The length of the list is", meLENT)

for x in range(meLENT):       

    #find the smallest number in the unsorted list

    miniMe = min(unsortedlisty)
    print("The smallest number is", miniMe)
    #eg this returns 1

    #add this minumum to the sortedlist (append)
    sortedlisty.append(miniMe)
    print("The sorted list is now", sortedlisty)

    #remove it from the first list
    unsortedlisty.remove(miniMe)
    print("With the min gone, it's now..", unsortedlisty)

    #rinse and repeat




