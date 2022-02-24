# python3
# call_center.py - Call center class which has three levels of employees: respondents, managers, and directors.
# Calls are assigned to available employees if they are able to handle the call.


class Employee:
    """
    Call center employee class.
    """
    def __init__(self, level, name):
        self.is_able = True
        self.level = level
        self.name = name

    def __str__(self):
        if self.is_able == True:
            return f"{self.__name__} {self.name} available."
        else:
            return f"{self.__name__} {self.name} unavailable."

    
class CallCenter:
    """
    Call center class which has three levels of employees: respondents, managers, and directors.
    Calls are assigned to available employees if they are able to handle the call.
    """
    def __init__(self):
        self.employees = {
            1: [],
            2: [],
            3: [],
        }
        self.titles = {
            1: 'respondent',
            2: 'manager',
            3: 'director',
        }

    
    def add_employee(self, employee):
        """
        Adds employees to the call center.
        """
        if employee.level in self.employees:
            self.employees[employee.level].append(employee)

    def dispatch_call(self, call_level):
        """
        Dispatches call to employees based on level and availability.
        """
        if call_level in self.employees:
            for employee in self.employees[call_level]:

                if employee.is_able == True:
                    employee.is_able = False
                    return print(f"Call is assigned to {self.titles[employee.level]} {employee.name}")

            if call_level < len(self.employees):
                return self.dispatch_call(call_level + 1)


        return print(f"No employees are available to handle a level {call_level} call at this time.")

    def __str__(self):
        return f"{self.employees}"


def example():

    names = [
        'Sue',
        'Rebecca', 
        "Bob",
        'Jim', 
        'Timmy', 
        'Sally',
        'James', 
        'Samuel', 
        'Sam', 
        'Devin', 
        'Dude', 
        'Duuuuude', 
        'Richous', 
        'Summer', 
        'Autumn', 
        'Spring', 
        'Winter', 
        'Yuki', 
    ]

    levels = [1, 2, 3]

    i = 1
    employees = []
    for name in names:
        if i % 7 == 0:
            level = levels[2]
        elif i % 4 == 0:
            level = levels[1]
        else:
            level = levels[0]
        employee = Employee(level, name)
        employees.append(employee)
        i += 1

    call_center = CallCenter()

    for employee in employees:
        call_center.add_employee(employee)

    
    calls = [2 if x % 5 == 0 else 1 for x in range(20)]

    for call in calls:
        call_center.dispatch_call(call)


if __name__ == "__main__":
    example()