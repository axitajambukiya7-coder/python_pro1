# Expense Tracker Project

expensesList =[] # list of expenses in from of dictionary
print("Welcome to Expense Tracker : Kharcha kam kiya karo ")

while True:
    print("=======MENU=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice : "))

#ADD Expense
    if(choice ==1):
        date= input("Kis date par kharcha kiya tha? : ")
        category= input("Kis type ka kharcha kiya? (Food, Travel, Makeup, Books) : ")
        description= input("Aue detail dedo : ")
        amount= float(input("Enter the amount : "))

        expenses={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }  
        expensesList.append(expenses)
        print("\n DONE bro.Expense is added succesfully")

# 2.  VIEW ALL EXPENSES
    if(choice ==2):
        if( len(expensesList)==0 ):
            print("NO Expenses Added. Jao pehle kharcha karo. ")
        else:
            print("=====Ye h apka sara expense =====")
            count= 1
            for eachKharcha in expensesList:
                print(f"Kharcha Number {count} -> {eachKharcha['date']}, {eachKharcha['category']}, {eachKharcha['description']}, {eachKharcha['amount']}")
                count= count+1

# 3. View Total Spending

    if(choice == 3):
        total= 0
        for eachKharcha in expensesList:
            total = total + eachKharcha["amount"]
        
        print("\n TOTAL KHARCHA = ", total)

# 4. Exit
    elif(choice == 4):
        print("Dhanyawad aapne humara system use kiya")
        break
    else:
        print("INVALID CHOICE. TRY AGAIN")