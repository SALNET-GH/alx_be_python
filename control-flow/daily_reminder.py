task = input("Enter your task: ")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no): ")


match priority.lower():
    case 'high':
        if time_bound == 'yes':
            print(f"reminder: {task} is a {priority_level} priority level task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"note: {task} is a {priority_level} priority level task. Consider completing it when you have free time.")
    
    case 'medium':
        if time_bound == 'yes':
            print(f"reminder: {task} is a {priority_level} priority level task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"note: {task} is a {priority_level} priority level task. Consider completing it when you have free time.")
    
    case 'low':
        if time_bound == 'yes':
            print(f"reminder: {task} is a {priority_level} priority level task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"note: {task} is a {priority_level} priority level task. Consider completing it when you have free time.")
    