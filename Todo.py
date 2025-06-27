todo_list=[]


def add_task():
    task=input("enter the task")
    todo_list.append({"task":task, "status":"pending"})
    print("new task added successfully")

def view_task():
    print("your to do list")
    if len(todo_list==0):
        print("no pending task")
    else:
         for index,task in enumerate(todo_list,1):
            print(f"{index}:{task['task']}-{task['status']}")
            print("\n")

def remove_task():
    print("your to do list")
    if len(todo_list==0):
        print("list is empty")
    else:
        try:
          search_index=int(input("enter the task number you want to remove"))-1
          if 0<=search_index < len(todo_list):
            remove_task=todo_list.pop(search_index)
            print(f"task Removed:{remove_task}")
          else:
            print("invaild task number")
        except ValueError:
            print("please enter valid task number")

def mark_task():
     if len(todo_list==0):
        print("list is empty")
     else:
        try:
          search_index=int(input("enter the task number you want to mark"))-1
          if 0<=search_index < len(todo_list):
            todo_list[search_index]['status']='done'
            print(f"task todo_list[search_index][task']has been marked be done")
          else:
            print("invaild task number")
        except ValueError:
            print("please enter valid task number")


def menu():
    while True:
        print("main menu")
        print("1.add a new task")
        print("2.view all task")
        print("3.remove a task")
        print("4.mark a task as completed")
        print("5.exit")

        choice=input("enter a number")
    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
         remove_task()
    elif choice=="4":
        mark_task()
    elif choice=="5":
        print("existing the application ")
        exit
    else:
      ("invalid choice try again")
menu()

