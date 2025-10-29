while True:
    reminder_status = input("Have you completed your task? (yes/no): ")
    if reminder_status == 'yes':
        print("Great job! Keep up the good work.")
        break
    elif reminder_status == 'no':
        print("please complete your task soon!")

