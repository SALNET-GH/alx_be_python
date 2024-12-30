task = input("Enter your task: ")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no): ")


match priority:
    case 'high':
        c_task = "is a high priority task"
    case 'medium':
        c_task = "is a medium priority task"
    case 'low':
        c_task = "is a low priority task"
if time_bound == 'yes':
    print(f"reminder: {task}{c_task} that requires immediate attention today!")
elif time_bound == 'no':
    print("reminder: {task}{c_task}. Consider completing it when you have free time.")
    