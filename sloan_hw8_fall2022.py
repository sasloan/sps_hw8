# header

def GetHeader(headerNum):
    
    print("====================================================================")
    print(f""" Welcome to hw 8 this is the header for the {headerNum} problem \n
          Please review the instructions for this specific problem below. Thank you.""")
    print("====================================================================")


# Problem 1

GetHeader(1)

print("")

print("""In this problem you will be asked to input 3 numbers. Then the program \n
      will calculate the numbers that you submit. Please not that if you input \n
      anything other than valid numbres the program will crash.""")
      
print("")
print("")
      
firstNum = round(float(input("Please input your first number: ")),2)
secondNum = round(float(input("Please input your second number: ")),2)
thirdNum = round(float(input("Please input your third number: ")),2)

def SumOfThree(paramater1, paramater2, paramater3):
    
        print("")
    
        recievedNumbers = [paramater1, paramater2, paramater3]
        
        print(f"The sum of the numbers that you entered is: {sum(recievedNumbers)}")
        

SumOfThree(firstNum, secondNum, thirdNum)

def AvgOfThree(paramater1, paramater2, paramater3):
    
        print("")
        
        recievedNumbers = [paramater1, paramater2, paramater3]
        
        print(f"The average of the number that you entered is: {sum(recievedNumbers)/3}")
        
AvgOfThree(firstNum, secondNum, thirdNum)

def BigOfThree(paramater1, paramater2, paramater3):
    
        print("")
        
        recievedNumbers = [paramater1, paramater2, paramater3]
        
        print(f"The Biggest of the numbers that you entered is: {max(recievedNumbers)}")
        
BigOfThree(firstNum, secondNum, thirdNum)

    
# Problem 2

GetHeader(2)

print("")

print("""Program two is designed to find the area of a shape, you will be asked \n
      to input the height of the shape and the width of the shape then you \n
      will receive an output of the area. Please note that if you input anything \n
      other than numbers the program will crash. Thank you.""")
      
print("")
print("")
      
hieght = round(float(input("Please input the hieght of your shape here: ")),2)
width = round(float(input("Please input the width of your shape here: ")),2)

def FindArea(paramater1, paramater2):
    
        print("")
        
        print(f"The area of your shape is: {paramater1 * paramater2}")
        
FindArea(hieght, width)


# Problem 3

GetHeader(3)

print("")

print("""Program three is desinged to tell you what the number value in a 1-800 \n
      number is when letters are provided to you. Please enter the 1-800 number \n
      you would like converted to numbers. example(1800WALMART) would be entered \n
      in and the program will show 18009256278.""")
      
print("")
print("")

last7 = input("Please input the 7 letters after the 1-800 in your number(do not include spaces and enter in all caps): ")

def LetterToNumber(paramater1):
    
        print("")
        
        
        
        if(len(paramater1) == 7):
            
            number = ''
            
            for letter in paramater1:
                for i in range (len(letter)):
                    if letter[i] in 'ABC':
                        number = number + '2'
                    elif letter[i] in 'DEF':
                        number = number + '3'
                    elif letter[i] in 'GHI':
                        number = number + '4'
                    elif letter[i] in 'JKL':
                        number = number + '5'
                    elif letter[i] in 'MNO':
                        number = number + '6'
                    elif letter[i] in 'PQRS':
                        number = number + '7'
                    elif letter[i] in 'TUV':
                        number = number + '8'
                    elif letter[i] in 'WXYZ':
                        number = number + '9'
                        
            print(f" Your number is: 1800{number}")
                  
        elif(len(paramater1) < 7):
            
            print("")
            
            print("I am sorry but you did not enter enough letters please run the program again.")
            
        elif(len(paramater1) > 7):
            
            print("")
            
            print("I am sorry bu you entered to many letters please run the program again.")

LetterToNumber(last7)
    


        