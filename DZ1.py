from sys import argv

script_name, working_hours, hourly_rate, bonus = argv
def work():
    try:

        working_hours = int(working_hours)
        hourly_rate = int(hourly_rate)
        bonus = int(bonus)
        salary = working_hours * hourly_rate + bonus

        print("Name script: ",  script_name, "\n"
        "Working hours: ", working_hours, "\n"
        "Hourly rate: ", hourly_rate, "\n"
        "Bonus: ", bonus, "\n"
        "Employee salary: ", salary)
    except ValueError:
        print("Not a number entered!")
work()