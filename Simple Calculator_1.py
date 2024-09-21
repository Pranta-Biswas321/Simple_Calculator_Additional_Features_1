#A simple calculator with Additional Features by Pranta Biswas

# Making functions to take multiple Integers or Floats as input 
# from the user and calculates their selected operation

def addnum():
    a1=int(input("How many numbers for Addition: ")) #Taking Input
    a2=input("Integer OR Float: ")                   #Taking Input
    a4=0                                             #Initializing variable to store sum

    if a2=="Integer":                                #Checking for Integer or Float
        for i in range(0,a1):                        #Loop to collect all numbers
            a3=int(input("Enter Integer: "))
            a4=a4+a3                                 #Adding all numbers

    elif a2=="Float":                                #Same process in case of Float
        for i in range(0,a1):
            a3=float(input("Enter Float: "))
            a4=a4+a3

    else:
        print("Provide Valid Input")                #Require Accurate Input

    print("SUM:",a4)
    print("\n")                                     #To Create Space between Displaying Menu and Executed Code


def subnum():
    s1=int(input("How many numbers for Subtraction: "))  #Taking Input
    s2=input("Integer OR Float: ")                       #Taking Input

    if s2=="Integer":
        s3=int(input("Enter Integer: "))                #Taking First Number
        for i in range(0,(s1-1)):
            s4=int(input("Enter Integer: "))
            s3=s3-s4                                   #Subtracting numbers from first digit

    elif s2=="Float":                                  #Same in case of Float
        s3=float(input("Enter Float: "))
        for i in range(0,(s1-1)):
            s4=float(input("Enter Float: "))
            s3=s3-s4

    else:
        print("Provide Valid Input")

    print("DIFFERENCE:",s3)
    print("\n")                                     #To Create Space between Displaying Menu and Executed Code

#Same Process as addition but with one Change
def mulnum():
    m1=int(input("How many numbers for Multiplication: "))
    m2=input("Integer OR Float: ")
    m3=1                                              #Multiplying anything with 0 gives 0 so initialized 1

    if m2=="Integer":
        for i in range(0,m1):
            m4=int(input("Enter Integer: "))
            m3=m3*m4

    elif m2=="Float":
        for i in range(0,m1):
            m4=float(input("Enter Float: "))
            m3=m3*m4

    else:
        print("Provide Valid Input")

    print("MULTIPLICATION:",m3)
    print("\n")                                     #To Create Space between Displaying Menu and Executed Code

#Same Process as subtraction with one Change
def divnum():
    try:                                #Incase of ZeroDivisionError
        d1=int(input("How many numbers for Division: "))
        d2=input("Integer OR Float: ")

        if d2=="Integer":
            d3=int(input("Enter Integer: "))
            for i in range(0,(d1-1)):
                d4=int(input("Enter Integer: "))
                d3=d3/d4

        elif d2=="Float":
            d3=float(input("Enter Float: "))
            for i in range(0,(d1-1)):
                d4=float(input("Enter Float: "))
                d3=d3/d4

        else:
            print("Provide Valid Input")

        print("DIVISION:",d3)
        print("\n")                                     #To Create Space between Displaying Menu and Executed Code
    except ZeroDivisionError:
        print("Error due to providing Zero as input")
        print("\n")                                     #To Create Space between Displaying Menu and Executed Code


#Displaying Menu
print("SIMPLE CALCULATOR")
while(True):
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter Your Choice (1,2,3,4,5): "))
    if choice==1:
        addnum()
    elif choice==2:
        subnum()
    elif choice==3:
        mulnum()
    elif choice==4:
        divnum()
    elif choice==5:
        break                #To Exit from the While Loop
    else:
        print("Provide a Valid Number")
        print("\n")                                     #To Create Space between Displaying Menu and Executed Code
