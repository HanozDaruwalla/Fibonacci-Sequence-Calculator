import time


#This Project Belongs To Hanoz Daruwalla (21483405) Algorithms And Datatypes Coursework 2021/2022

def Fibonacci_Num_Finder(User_Input,Number1,Number2,New_Number,Counter):


    if Counter == (User_Input+1):#if recursion is on the increment number entered by the user
        print("\nNumber", Counter-1, "of the Fibonacci Sequence is", New_Number)
        print("\nThis Project Belongs To Hanoz Daruwalla (21483405) Algorithms And Datatypes Coursework 2021/2022\n")
        return New_Number
    else:#if it is not on the increment number entered by the user, change variables and output

        if Counter <2:
            print("Step", Counter, ":  ", Number1, "+", Number1, "= ---------- ", Number1)
            Counter = Counter +1
            print("Step", Counter, ":  ", Number1, "+", Number2, "= ---------- ", Number2)
            Counter = 2
            Fibonacci_Num_Finder(User_Input,Number1,Number2,New_Number,Counter)
        else:
            New_Number = Number1 + Number2
            print("Step", Counter, ":  ", Number1, "+", Number2, "= ---------- ", New_Number)
            Number1 = Number2
            Number2 = New_Number
            Counter += 1
            Fibonacci_Num_Finder(User_Input,Number1,Number2,New_Number,Counter)
        
        


def start():#runs at start of program. make sure input is a int
    # This Project Belongs To Hanoz Daruwalla (21483405) Algorithms And Datatypes Coursework 2021/2022
    
    print("\nThis Project Belongs To Hanoz Daruwalla (21483405) Algorithms And Datatypes Coursework 2021/2022\n")
    User_Input = input("Which Fibonacci sequence number would you like to find? ")

    Number1 = int(0)
    Number2 = int(1)
    New_Number = int(66)#66 is random
    Counter = int(0)

    if User_Input.isdigit():
        User_Input = int(User_Input)
        print("\nFibonacci number finder activated")
        print("-------------------------------------\n")
        Fibonacci_Num_Finder(User_Input,Number1,Number2,New_Number,Counter)

    else:#if not wait 3 seconds and restart
        print("\nThat was not a number. !! Restarting in 3 Seconds !! ")
        time.sleep(3)
        print("\n\n\n\n")
        start()


start()
