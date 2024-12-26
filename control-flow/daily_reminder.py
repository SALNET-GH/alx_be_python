task = input("Enter your task: ")
priority_level = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no): ")


match time_bound.lower():
    case 'yes':
        print(f"reminder: {task} is a {priority_level} priority level task that requires immediate attention today!")
    case 'no':
        print(f"note: {task} is a {priority_level} priority level task. Consider completing it when you have free time.")