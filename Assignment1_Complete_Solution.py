# Course: ITI 1120
# Soultions
# Created By
# Tarundeep Singh
# tsing056@uottawa.ca


# Q1)Input three numbers from the user, compute their sum and output the sum to the screen. 

print ("Please enter three numbers(Press Enter):")       #Asking for the User Input for addition of 3 numbers

userInputNumber = input("First number:")          #Asking user for the first number
firstNumber = int(userInputNumber)				  #Converting the Input to integer 	

userInputNumber = input("Second number:")         #Repeating for second number
secondNumber = int(userInputNumber)

userInputNumber = input("Third number:")          #Repeating for third number
thirdNumber = int(userInputNumber)                  

print("The required sum is:", firstNumber+secondNumber+thirdNumber) 

print("End of Program 1 Press Enter for Program 2")
# End of Program 1

# Q2)Input three positive numbers from the user. Make sure each of the three numbers is
# positive (greater than zero). Each time the user inputs an invalid number for input, 
# you will give them an error message, and ask them to input another number. There is 
# no limitation on how many times a user can input a wrong value. 

#Start of Program 2

count = 1     #Assigning a starting value to counter variable
print("Please enter Three Positive Numbers:")   #Asking for the User Input for addition of 3 positive numbers

while count != 4:                 #Begining loop for getting input from user Ends when user has entered three positive numbers
    dispCount = str(count)     #Turn counter to string to display it in the prompt
    userInputNumber = input("Enter Number "+dispCount+":")   #Prompt user to enter number
    checkInput = int(userInputNumber)          #Turn input to integer to check
    if checkInput > 0:
        count = count + 1       #If number is + add 1 to counter
    else:
        print("Sorry, ", userInputNumber,"is not a positive number.Please try again.")    #If user entered a negative number display error and start again

#End of Program 2 

# Q3) Repeat (b), imposing a limit of three wrong attempts for each number, after which you quit the program. 

#Start of Program 3 

counter = 1     #Assign a starting value to counter
errorcount = 0	#Maintaining counter to allow only permissible number of attempts
print("Please enter three positive numbers..3 attempts are permitted")   #Provide instruction to user to enter

while counter != 4 and errorcount != 3:            #Begin loop where user will be prompted to enter numbers. Ends when 3 + numbers entered or after 3 errors
    dispCount = str(counter)               #Turn counter to string to display it in the prompt
    userInputNumber = input("Enter Number "+dispCount+":")       #Prompt user to enter number
    checkInput = int(userInputNumber)                    #Turn input to integer to check
    if checkInput > 0:
        counter = counter + 1                 #If number is + add 1 to counter
    else:                                                   #If number is not positive
        errorcount = errorcount + 1                                       #error counter increases by 1
        print("Sorry,", userInputNumber,"is not a positive number.")    #Error message
        print(3-errorcount," attempts remaining...")             #Display remaining attempts
print("You have exceeded the maximum number of permissible limits so the program is now exiting")  


# End of Program 3

# Q4) Input a Celcius temperature from the user, convert it to Fahrenheit, and output the Fahrenheit temperature.

# Start of Program 4 

print("Converting temperature from Celcius to Fahrenheit")         #Provide insturction to user about the program
userInputCelcius = input("Enter temperature in Celcius:") #Prompt user to enter value in celcius
celcius = int(userInputCelcius)                        #Turning the required input to an integer
print("Farenheit temperature: ",celcius * 1.8 + 32)     #Print value after the conversion using the conversion formulae

# End of Program 4

# Q5) Ask the user for their name, and then greet them with their name, 
# saying “Hello there, <name>”. Where <name> is the name input by the us

# Start of Program 5

userInputName = input("What is your name? ")    #Prompts user to enter their name
print("Hello there, ", userInputName)             #Prints message followed by user's name as required.

# End of Program 5

# Q6) Print the number six multiplied by numbers from 1 to 10, 
# each one on a line. You need to perform the computation first 
# before printing it (don’t just compute it in your head and print it using a message).

# Start of Program 6

tablecounter = 1             #Assign starting value to counter
print("Multiplication of Number 6")     #Displaying what will be done in this program
while tablecounter != 11:    #Will loop 10 times as required
    print("6 x", tablecounter,"=", 6*tablecounter)    #Print the required output using the loop Counter
    tablecounter = tablecounter + 1   #Counter increases by 1 after each repetition

print("Mutplication Completer")     #Completition of Required Multiplication   

# End of Program 6

# Q7) a.  Print numbers from 1 to 20 (you must use a counter that starts with 1, 
# some looping mechanism like we did in class, and make sure you increment the counter inside the loop properly).

# Start of Program 7

print("Printing Numbers from 1 to 20 using the counter method")
numCounter = 1     #Assign starting value to numbercounter
while numCounter != 21:    #Loop for 20 repititions as required
    print(numCcounter)      #Pring value of number counter
    numCounter = numCounter + 1   #Increase counter value by 1 after each repitition
print("Required Printing is complete")  

# End of Program 7

# Q8) a.  Input a salary, and compute and output a basic tax on the salary as such: 
# a.  If the salary is in [0-50000[ , the tax is 15 percent.
# b.  If the salary greater than or equal to 50000, the tax is 25 percent.

# Start of Program 8

loopcontrol = 0                 #Variable used to control loop on next line
while loopcontrol == 0:         #Loop until input from user is valid
    userInputSal = input("Enter a salary for tax calculation: ")    #Prompt user to enter salary to calculate tax
    salary = int(userInputSal)                 #Turn input into integer for easy calculation
    if salary > 0:                          #If salary is positive condition is met and loop ends and tax caluation starts
        loopcontrol = 1
    else:
        print("Invalid salary. Try again")  #If salary is not positive. Error message to try again

if salary <= 50000:        
    print("For a salary of ",salary, "a 15% tax applies equalling:", salary*0.15)   #If salary is less than or equal to 50000 then applying corresponding tax
else:                       
    print("For a salary of ",salary, "a 25% tax applies equalling:", salary*0.25)   #If salary is greater than 50000 then applying corresponding tax

# End of Program 8

# Q9) Input two numbers from the user, swap the two numbers (using a third memory location), 
# and output the numbers to the screen after swapping    

# Start of Program 9

print("Enter two numbers for swapping")    #Instruction for user
num1 = input("Number 1: ")       #Prompt user to enter first number
num2 = input("Number 2: ")       #Prompt user to enter second number
temp = num1
num1 = num2       #Swtich numbers using third temp variable
num2 = temp
print("swaping...")     #Providing feedback to user
print("Number 1:", num1)     #Print numbers after switch
print("Number 2:", num2)

print("Swapping Complete!")

# End of Program 9

# Q10) a. Input two numbers from the user, and print the number that has the higher value to the screen.

#Start of Program 10

print("Please enter two numbers for checking")       #Instruction to user to enter numbers
userInputNum = input("Number 1: ")         #Prompt user to enter a number
num1 = int(userInputNum)                #Change input to integer
userInputNum = input("Number 2: ")
num2 = int(userInputNum)

if num1 > num2:           #If first number is greater, print first number
    print("The greater number is Number 1:", num1)
else:                           #If second number is greater, pring second number
    print("The greater number is Number 2:", num2)

#End of Program 10    













