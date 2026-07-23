# JOSH TO DO LIST(CALENDER)

print ("----- JOSH TO DO LIST -----")

print("""1. Add task
2. View tasks
3. Remove task
4. Exit""")

total_list = []



while True:
    user_enter = input("choose option from the menu above: ").strip()

    if  user_enter == "1":
        global task
        task = input("Enter your task: ")
        if task == "":
            print("task cannot be empty")
            task = input("enter your task: ")
        if task != "":
            print("task added succesfully!")
        elif task != "":
            print ("task added succesfully!")
        enter = input("enter q to quit ")
        total_list.append(task)
        if enter.lower == "q":
            break

    if user_enter == "2":
        shit = 0
        for i in total_list:
            shit += 1
            print(f"{shit}. {i}") 
            
    if user_enter == "3":
        time = 0
        for me in total_list:
            time += 1
            print (f"{time}. {me} ")
            
            print()

        change = input("Enter task to remove: ")
        if total_list == []  or total_list == "":
            print("the folder is empty")
        elif change == "":
            print("this cant be empty, please input something")
            change = input("Enter task to remove: ")
        
        for phone in total_list:
            if change in phone:
                total_list.remove(phone)
                print("task removed succesfully !")
                break 
        if change != phone:
            print(f"{change} is not added, please add {change} in the add section ")   
            
    if user_enter == "4": 
        print("Thank You For Using Josh To Do List 🤗")
        break
    
            
    