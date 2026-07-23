
# for user to put thier names and get to know them
user_name = input ("enter your name ")
print (f"welcome {user_name} !!")

print (" ------- JOSH EXPENSE TRACKER 😎 -------")

add_expense  = print("1.ADD EXPENSES ")
view_expense = print("2.VIEW EXPENSES ")
total_expense= print("3.TOTAL EXPENSES ")
exit = print ("4.EXIT")




# making everything run through a while loop, so it keep asking the users if they put a wrong password
while True:
      combination = input ("choose your option from the above menu: ").strip()
      if combination.lower() == "1": # adding expenses
         expense = input ("enter your expense name ")
         try:
            amount = int (input("enter expense amount "))
         except ValueError:
              print("amount must be number")
              amount = int(input("enter expense amount "))     
         exit = input("q to quite ")
         with open ("tracker.txt", "a") as file:
              file.write(f"EXPENSE: {expense} ")
              file.write(f"AMOUNT: {amount} \n")
         if exit.lower() == "q":
            print("thank you for using josh expense tracker 🤗 !!")
      elif combination.lower() == "2": # viewing expenses
         with open ("tracker.txt","r") as file:
             for lines in file:
                 print(file.read(), end=" ")
      elif combination.lower() == "3": # calculating the expenses
         with open ("tracker.txt","r") as file:
                total = 0
                for lines in file:
                    parts = lines.split("AMOUNT: ")
                    if len(parts) > 1:
                        amount_str = parts[1].strip()
                        try:
                            amount = int(amount_str)
                            total += amount
                        except ValueError:
                            print(f"Invalid amount found: {amount_str}")
                print(f"Total expenses: {total}")
             
            

                 
      elif combination.lower() == "4": # exiting josh expense tracker app
           print("thank you for using josh expense tracker 🤗 !!")
           break

        #my love for you is like a moving train, it can never stops
        # burst my head 😂