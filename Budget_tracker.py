
def main():
    print('WELCOME TO THE BUDGET TRACKER')
    Total_budget=float(input('ENTER YOUR TOTAL BUDGET:'))
    print('YOUR TOTAL BUDGET IS :',Total_budget )
    remaining_budget = Total_budget

    while True:
        print('\nWHAT WOULD YOU LIKE TO DO NOW?')
        print('1. ADD EXPENSES')
        print('2. SHOW REMAINING BUDGET')
        print('3. END')

        selection=int(input('ENTER THE NUMBER OF YOUR CHOICE(1-3):'))

        if selection == 1:
           expense=float(input('ENTER YOUR EXPENSE AMOUNT:'))
           if expense > remaining_budget:
             print('EXPENSE EXCEEDS YOUR BUDGET')
           else:

               remaining_budget-=expense
               print('DO YOU WANT TO KNOW YOUR REMAINING BUDGET:')
               print('1.YES')
               print('2.NO')

               choice = int(input('ENTER YOUR CHOICE(1 OR 2):'))

               if choice == 1:
                  print('YOUR REMAINING BUDGET IS :' , remaining_budget)
               elif choice == 2:
                    print('OKAY THANK YOU')


        elif selection == 2:
             print('YOUR REMAINING BUDGET IS :' , remaining_budget)


        elif selection == 3:
             print('EXITING BUDGET TRACKER')
             break
    else:
        print('INVALID CHOICE. PLEASE MAKE A VALID CHOICE:')


main()
