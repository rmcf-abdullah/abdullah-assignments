oddList = [] # this creates an empty list

for i in range (0,10): #for loop iterating through 10 times 

    numOne = int(input("Please enter the number as an integer:")) #retrieve integer value 
    tempNum = numOne #assigning temp value
    numOne = (numOne % 2) #gets remainder from number one and assigns to itself 
    
    if numOne == 1: #if statement to check if numOne equates to 1 
        oddList.append(tempNum) #append tempNum from list 


print ("The greatest odd number is " + str(max(oddList))) #print stmnt




