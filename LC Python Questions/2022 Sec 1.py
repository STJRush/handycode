def func(a): # I take my 5 aeros with me to Vegas
    
    a = a + 1 # I get another 1 aero in Vegas
    b = 15 # I buy 15 bounties in Vegas
    print(a) # I buy 5 + 1 = 6 aeros in Vegas with me now
    print(b) # Still have those 15 bounties, don't return with them
    
    return(a) # I return to ireland with 6 aeros in my pocket



# Starts here

a = 5 # 5 aeros in Ireland
b = 10 # 10 bounties aeros in Ireland

print(a)  # I still have 5 aeros

# the vegas trip happens
b = func(a)

print(a)
print(b)