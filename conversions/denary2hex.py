startNumber= 845

remainderList = []
remainderListWithLetters=[]

wholeNumber = startNumber #the first whole number is your starting number

print("Rough work")

while wholeNumber>0: #stops dividing at zero
    
    remainder = wholeNumber%16  #finds remainder after being divided by 16
    wholeNumber=wholeNumber//16  #finds next whole number
    
    print(wholeNumber, " r", remainder) #prints it
    remainderList.append(remainder) #adds it to a list
    
print("\n With numbers only \n")
remainderList.reverse() #reverses list to read answer bottom up
print(remainderList)


#this bit converts the numbers 10-15 into letters A-F
print("\n With proper letters \n")
for num in remainderList: #check each number in the list

    if num==10: #if it's 10, make it A instead.
         num="A"
         remainderListWithLetters.append(num) #add to final list
    elif num ==11:
         num="B"
         remainderListWithLetters.append(num)
    elif num ==12:
         num="C"
         remainderListWithLetters.append(num)
    elif num ==13:
         num="D"
         remainderListWithLetters.append(num)
    elif num ==14:
         num="E"
         remainderListWithLetters.append(num)
    elif num ==15:
         num="F"
         remainderListWithLetters.append(num)
    else:
         remainderListWithLetters.append(num)
        
print(remainderListWithLetters)


