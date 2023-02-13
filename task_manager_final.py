# ========== Importing Libraries =========== #

from datetime import date
import datetime


# =========== Functions =========== #

def write_task_data(users_tasks_dict):
# Rewriting the text file with the updated data
    with open("tasks.txt", "w+") as file:
        for key, value in users_tasks_dict.items():
            tasks_string = ", ".join(value)
            file.write(tasks_string)

def reg_user():
# Registering a new user - username & password 
    print('------------------------------------------------------ \n You can add a new user by entering their details below. \n') 
    new_username = input("Username: ")  
    while new_username in user_dictionary:
        new_username = input("User already exists. Please enter a new username to register a new user: ")
    new_password = input("Password: ")
    password_confirmed = input("Confirm password: ")
    while new_password != password_confirmed:
        print("The passwords do not match. Please try again.")
        new_password = input("Password: ")
        password_confirmed = input("Confirm password: ")
    user_dictionary[new_username] = new_password
    users_data = open("user.txt", "a")      
    users_data.write("\n" + new_username + ", " + new_password)
    users_data.close()
    print(f"\n \nThank you, {new_username} has been added to the users.")
    

def add_task(): 
# Adding a new task - requesting details of the task from the user 
    """ 
    NOTE: I allow the user to add tasks to users that aren't registered yet,
    in case they want to add tasks for a new starter, who hasn't been registered as a user yet. 
    If we didn't want to allow it I'd add an if statement to check if username is in the user list,
    and if not, I'd print an error message eg. "User doesn't exist, please enter a valid/existing username." 
    """

    print('\n\n------------------------------------------------------ \n You can add a new task below by providing the required details. / Whilst adding these details, please make sure that if you use commas (",") you do NOT add a space after the comma. Thank you!/  \n') 
    task_assigned_to = input("Which user is this task assigned to? ")  
    task_title = input("Task title: ")
    task_description = input("Description of the task: ")
    date_assigned = str(date.today().strftime('%d %b %Y'))
    due_date = input("Due date of the task (please make sure you enter the date in the following format: '10 Oct 2019'): ")
    tasks_data = open("tasks.txt", "a")
    tasks_data.write("\n" + task_assigned_to + ", " + task_title + ", " + task_description + ", " + date_assigned + ", " + due_date + ", " "No") 
    tasks_data.close()
    print(f"\n \nThank you, the task ({task_title}) has been added to the tasks.\n")


def view_all():
# Printing all the tasks with index numbers
    print('\n\n------------------------------------------------------ \n\nYou can see all the existing tasks below: \n\n') 
    tasks_data = open("tasks.txt", "r")
    tasks = tasks_data.readlines()
    tasks_data.close()

    for pos, line in enumerate(tasks,1):
        split_tasks = line.split(", ")
        
        task_nr = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ [ {pos} ] ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
        task_assigned_to = split_tasks[0]
        task = split_tasks[1]          
        task_desc = split_tasks[2]
        date_assigned = split_tasks[3]
        due_date = split_tasks[4]
        task_status = split_tasks[5]
    
        print(f"""\n\n {task_nr} \n\n
Assigned to:\t\t {task_assigned_to}\n
Task:\t\t\t {task} \n
Description: \t\t {task_desc} \n
Date assigned:\t\t {date_assigned} \n
Due date:\t\t {due_date} \n
Completed?\t\t {task_status}
        """)

def view_mine():
# Printing the tasks assigned to the logged in user
    tasks_data = open("tasks.txt", "r")
    tasks = tasks_data.readlines()
    tasks_data.close()

    users_tasks_dict = {}

    for pos, line in enumerate(tasks,1):    
        split_tasks = line.split(", ")
        users_tasks_dict[pos] = split_tasks
        if username == split_tasks[0]:
            output = f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ [ Task number: {pos} ] ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n"
            output += "\n"
            output += f"Assigned to:\t \t {split_tasks[0]}\n"
            output += f"Task: \t \t \t {split_tasks[1]}\n"               
            output += f"Description: \t \t {split_tasks[2]}\n"
            output += f"Date assigned: \t  \t {split_tasks[3]}\n"
            output += f"Due date: \t \t {split_tasks[4]}\n"
            output += f"Completed:\t \t {split_tasks[5]}\n"
            output += "\n"
            print(output)

    # Editing the task
    while True:
        try:
            task_nr = int(input('''To edit a task please enter the task number.\n\nEnter -1 to return to the main menu. '''))

            if task_nr == -1:
                break
            
            if users_tasks_dict[task_nr][0] == username:
                selected_task = tasks[task_nr-1]   
                split_selected_task = selected_task.split(", ")

                if users_tasks_dict[task_nr][-1].strip("\n") == "No":
                    task_action = input('''\n\nPlease choose from the below options:\n
                    c - mark the task as complete
                    e - edit the task
                    -1 - exit \n\n''').lower()

                    # Mark the task 'completed'
                    if task_action == "c":
                        users_tasks_dict[task_nr][-1] = "Yes\n"
                        print ("This task has been marked completed.")    
                        break
                    
                    # Editing the task 
                    elif task_action == "e":

                        output = """ \n\n --------------- [ SELECT AN OPTION ] ------------------- \n 
    1, Assign the task to another user
    2, Change the due date of the task
    3, Update the task description 
    4, Exit \n \n """

                        task_edit = int(input(output))
                        
                        if task_edit == 1: 
                            task_assigned_to_new_user = input("\n\n Please enter the name of the user you'd like to reassing this task: \n")
                            users_tasks_dict[task_nr][0] = task_assigned_to_new_user

                            print(f"\n\n Thank you, {username.capitalize()}. This task has been assigned to {task_assigned_to_new_user}.\n" )
                            break

                        elif task_edit == 2:
                            new_due_date = input("Please enter the new due date: \n")
                            users_tasks_dict[task_nr][-2] = new_due_date

                            print(f"\n\n Thank you, {username.capitalize()}. The due date of this task has been updated to {new_due_date}.\n" )
                            break

                        # THIS PART IS NO LONGER IN THE TASK DESCRIPTION. IT WAS THERE WHEN I STARTED WORKING ON THIS TASKS, AND AS IT WORKS I DIDN'T WANT TO DELETE THIS PART.
                        elif task_edit == 3:
                            if split_selected_task[-1].strip("\n") == "No":
                                new_description = input("\n\n Please enter the new task description (if using commas, please do NOT add a space after the comma):\n")
                                users_tasks_dict[task_nr][2] = new_description

                                print(f"\n\n Thank you, {username.capitalize()}. The task description has been updated.\n\n")
                                break
                        elif task_edit == 4:
                            break

                    if task_action == "-1":
                        break

                    else:
                        print("\n\nInvalid selection, please try again.\n\n")
                        continue

                else:
                    print("\n\n Only incomplete tasks can be edited.\n\n")

            else:
                print("\n \n Invalid selection, you can only edit your own tasks. Please try again.\n ")       

        except ValueError:
            print("\n\nInvalid input, please enter a task number.\n\n")
            continue
    
    tasks_data = open("tasks.txt", "w+")
    write_task_data(users_tasks_dict)
    tasks_data.close()
    

def task_overview():
    task_data = open("tasks.txt", "r")
    tasks = task_data.readlines()
    tasks_data.close()

    tasks_total_nr = len(tasks)

    # counter variables
    completed_tasks_nr = 0
    uncompleted_tasks_nr = 0
    overdue_tasks_nr = 0

    # Checking if the task is completed or not --> counting completed & incomplete tasks
    for line in tasks:
        split_task = line.split(", ")
        if split_task[-1] == "Yes" or split_task[-1] == "Yes\n":
            completed_tasks_nr += 1
        else:
            uncompleted_tasks_nr += 1

    # Checking if the task is overdue
    for line in tasks:
        split_task = line.split(", ")
        due_date = split_task[-2]
        date_format = '%d %b %Y'
        date_obj = datetime.datetime.strptime(due_date, date_format)

        if split_task[-1] == "No" or split_task[-1] == "No\n":
            if date_obj < datetime.datetime.today():
                overdue_tasks_nr += 1 

    incomplete_tasks_percentage = round(uncompleted_tasks_nr / tasks_total_nr * 100, 2)
    overdue_tasks_percentage = round(overdue_tasks_nr / tasks_total_nr * 100, 2)

    tasks_overview = open("tasks_overview.txt", "w+")
    tasks_overview.write(f""" \n\n --------------- [ Tasks Overview ] ------------------- \n
The total number of tasks: {tasks_total_nr}.    
The total number of completed tasks: {completed_tasks_nr}.
The total number of uncompleted tasks: {uncompleted_tasks_nr}. 
The total number of overdue tasks: {overdue_tasks_nr}.
The percentage of tasks that are incomplete: {incomplete_tasks_percentage}%.
The percentage of tasks that are overdue: {overdue_tasks_percentage}%.\n\n""")

    tasks_overview.close()

def user_overview():
    users_data = open("user.txt", "r")
    users = users_data.readlines()
    users_data.close()

    tasks_data = open("tasks.txt", "r")
    tasks = tasks_data.readlines()
    tasks_data.close()

    tasks_total_nr = len(tasks)
    nr_of_users = len(users)

    # Counter variables
    users_tasks = 0 
    users_completed_tasks = 0
    users_uncompleted_tasks = 0
    overdue_task_nr = 0

    # Creating dictionaries to save each data linked to each user
    users_tasks_dict = {}
    users_tasks_percentage_dict = {}
    completed_tasks_dict = {} 
    incomplete_tasks_dict = {}
    completed_task_percentage_dict = {}
    incomplete_task_percentage_dict = {}
    overdue_task_dict = {}
    overdue_task_percentage_dict = {}

    # Looping through the users and the task lines - checking each user against each task line to count the required data (completed, incomplete, overdue)
    for k in user_dictionary:
        for line in tasks:
            split_task = line.split(", ")
            split_task[-1] = split_task[-1].strip("\n")

            if k == split_task[0]:
                users_tasks += 1 

                if split_task[-1] == "No":
                        users_uncompleted_tasks += 1

                else:
                        users_completed_tasks += 1

                due_date = split_task[-2]
                date_format = '%d %b %Y'
                date_obj = datetime.datetime.strptime(due_date, date_format)

                if split_task[-1] == "No" and date_obj < datetime.datetime.today():
                        overdue_task_nr += 1 
            overdue_task_dict[k] = overdue_task_nr                
 
        # Saving the results into dictionaries
        users_tasks_dict[k] = users_tasks
        users_tasks_percentage_dict[k] = round(users_tasks_dict[k] / tasks_total_nr * 100, 2)
        completed_tasks_dict[k]  = users_completed_tasks
        incomplete_tasks_dict [k] = users_uncompleted_tasks
        
        if users_tasks != 0:
            completed_task_percentage_dict[k] = round(completed_tasks_dict[k] / users_tasks * 100, 2)
            incomplete_task_percentage_dict [k] = round(incomplete_tasks_dict[k] / users_tasks * 100, 2)
            overdue_task_percentage_dict[k] = round(overdue_task_dict[k] / users_tasks * 100, 2)

        # To avoid 0 division error, setting these values to 0 in case the user doesn't have any tasks    
        else:
            completed_task_percentage_dict[k] = 0
            incomplete_task_percentage_dict[k] = 0
            overdue_task_percentage_dict[k] = 0

        # Resetting the counters at the end of the loop, so the count can start again for the next user
        users_tasks = 0 
        users_completed_tasks = 0
        users_uncompleted_tasks = 0
        overdue_task_nr = 0

    user_overview_file = open("user_overview.txt","w+") 

    user_overview_file.write(" ---------------------------------- [ User Overview ] ----------------------------------   \n")

    for k in user_dictionary:
        user_overview_file.write(f"""
        \n --------------- {k}'s tasks overview -------------------- \n 
        Number of tasks: {users_tasks_dict[k]}
        Percentage of total tasks: {users_tasks_percentage_dict[k]}.
        Completed tasks: {completed_tasks_dict[k]}
        Uncompleted tasks: {incomplete_tasks_dict[k]}
        Percentage of completed tasks: {completed_task_percentage_dict[k]}%.
        Percentage of incomplete tasks: {incomplete_task_percentage_dict[k]}%.
        Overdue tasks: {overdue_task_dict[k]}.
        Percentage of overdue tasks: {overdue_task_percentage_dict[k]}%.\n""")

    user_overview_file.close()

def display_statistics():
    # Calling the generate report functions in case they haven't been generated before
    task_overview()
    user_overview()
    
    # Reading and printing the data
    tasks_stats = (open("tasks_overview.txt", "r")).readlines()
    user_stats = (open("user_overview.txt", "r")).readlines()

    for line in tasks_stats:
        print(line)

    for line in user_stats:
        print(line)


# ==================== Login Section ========================== #

# Creating a dictionary for usernames & passwords
users_data = open("user.txt", "r")
tasks_data = open("tasks.txt", "r")

tasks = tasks_data.readlines()
users = users_data.readlines()

users_data.close()
tasks_data.close()

user_dictionary = {}    

for line in users:
    k, v = line.split(", ")
    user_dictionary[k] = v.strip("\n")

username = input("Username: ")
while username not in user_dictionary:      
    print("Invalid username. Please try again.")
    username = input("Username: ")

password = input("Password: ")
correct_password = user_dictionary.get(username)

while password != correct_password:
    print("Incorrect password.Please try again.")
    password = input("Password: ")

print(f"\n\nWelcome, {username.capitalize()}! You have sucessfully logged in. \n")   


# ========= Menu Section ========== #


# Menu for ADMIN:
while True:
    if username == "admin":
        menu = input('''------------------------------------------------------ \n \nSelect one of the following options below:\n
    r - Register a new user
    a - Add a task
    va - View all tasks
    vm - View my tasks
    gr - Generate reports
    ds - Display statistics
    e - Exit
    \n\n\n''').lower()   

# General Menu:    - Generate reports should be included for other users too? 
    else: 
        menu = input('''------------------------------------------------------ \n \nSelect one of the following options below:\n
    r - Register a new user
    a - Add a task
    va - View all tasks
    vm - View my tasks
    e - Exit
    \n\n\n''').lower()   

# Menu options & actions: 
    if menu == 'r' and username == "admin":
        reg_user()

    elif menu == 'r' and username != "admin":
        print("\n\nYou don't have permission to add new users.")

    elif menu == 'ds' and username == "admin":
        display_statistics()
    
    elif menu == 'a':
        add_task()
    
    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()
        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    elif menu == 'gr':
        task_overview()
        user_overview()
        print("\n\nThe reports have been generated and saved in the main folder. To view these reports please select the 'Display Statistics' option.\n")

    else:
        print("\n\nInvalid option, please try again. ")
