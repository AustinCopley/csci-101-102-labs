    #   Austin Copley
    #   ​CSCI 102 – Section B
    #   Week 4B - Todo List
number_of_tasks = 0
lots_to_do = 7
not_much_to_do = 4
print('Welcome to the TODO List tracker! Please enter the tasks that you need to do this week. To stop entering tasks, enter "DONE" (without quotation marks).')
todo_list = list()
while number_of_tasks >= 0:
    task = input("LIST> ")
    if task == "DONE":
        break
    else:
        todo_list.append(task)
number_of_tasks = len(todo_list)
if number_of_tasks > lots_to_do:
    print('You have', number_of_tasks, 'tasks to do. You have a lot to do! You better get to work!')
    print('OUTPUT', number_of_tasks)
    print('OUTPUT BUSY')
elif number_of_tasks < not_much_to_do:
    print("You have", number_of_tasks, "tasks to do. You don't have much to do, enjoy a break!")
    print('OUTPUT', number_of_tasks)
    print('OUTPUT FREE')
else:
    print("You have", number_of_tasks, "tasks to do. You are moderately busy.")
    print('OUTPUT', number_of_tasks)
    print("OUTPUT MODERATELY")
