alarm = dict(Masha=['7.00', '7.10', '7.20'], Pasha=['7.00', '5.00'], Maryna=['7.00', '8.00'],
             Vasya=['7.00'], Kolya=['7.00'], Kostya=[])

username = input("Enter username:")
operation = input("What do you want to do (set the alarm - type 'set'; delete the alarm - type 'delete' :")


def manage_the_alarm(username, operation):
    if username in alarm:
        if operation == 'set':
            new_alarm = input('set new alarm time: ')
            alarm[username].append(new_alarm)
            print(username, "has alarms at:", alarm[username])
        elif operation == 'delete':
            if len(alarm[username]) == 0:
                print("There is no alarm to delete")
            else:
                alarm_to_remove = input('which alarm to remove: ')
                alarm[username].remove(alarm_to_remove)
                print(username, "has alarms at:", alarm[username])
        else:
            print("You need to define: set of delete the alarm")
    else:
        print('User is not found :c')


manage_the_alarm(username, operation)
