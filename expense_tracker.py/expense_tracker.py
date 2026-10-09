expenses =[]

while (True):

    print("---- EXPENSIVE TRACKER-----")
    print("1. add expenses")
    print("2.View expenses")
    print("3. Total expenses")
    print("4.exit")

    choice = int (input("enter your choice:"))

    if choice == 1:
        name = input ("enter expense name ")
        amt= float(input("enter the amount"))

        expenses.append([name,amt])
        print("expense added successfully ")

    elif choice ==2:
        print("your expenses :")
        for item in expenses:
            print(f"{item[0]}: rs. {item[1]}")

    elif choice ==3:
        total=0
        for item in expenses:
            total += item[1]


        print("total expenses: Rs", total)

    elif choice == 4:
        print (" Thank you !!  you are exiting expense Tracker ")


    else:
        print ("You have entere a wronng choice , please try again ")





              

                  





 