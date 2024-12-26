task = input("Task: ")
priority_level = input("priority level (high,medium,low): ")
time_sensitive = input("time sensitive (yes/no): ")

match time_sensitive.lower():
    case 'yes':
        print(f"reminder: {task} is a {priority_level} priority level task that requires immediate attention today!")
    case 'no':
        print(f"note: {task} is a {priority_level} priority level task. Consider completing it when you have free time.")