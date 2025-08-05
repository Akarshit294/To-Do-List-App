def read():
    l =[]
    with open("todo.txt") as f:
        for i in f:
            l.append(i.strip())
    return l

def view():   
    l = read() 

    print("\n-----ToDo List-----\n")
    for i in range(len(l)):
        print(f"{i+1}>", l[i], end = "\n")
    print("-------------------")

def write(l):
    with open("todo.txt", "w") as f:
        for i in l:
            i += "\n"
            f.write(i)

def add():
    l = read()

    task = input("\nEnter a new task: ").strip()
    l.append(task)
    print("Task added successfully.")

    write(l)

def remove():
    l = read()

    rmv = input("\nEnter the task number to be removed:")
    l.pop(int(rmv)-1)
    print("Task removed successfully.")

    write(l)


print("\n----------Welcome to the ToDo List Application----------")
while(1):
    print("\n1. View ToDo list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit the Application")
    x = input("Enter your choice: ")

    if x == '1':
        view()
    elif x == '2':
        add()
    elif x == '3':
        remove()
    elif x == '4':
        print("\n----------Good Bye!----------")
        break
    else:
        print("\nPlease enter a valid choice.")
