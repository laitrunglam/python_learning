from abc import ABC,abstractmethod

class Employee :
    def __init__(self, employee_id, name):
        self.employee_id=employee_id
        self.name=name

    def display_info(self):
        print(f"MA NV : {self.employee_id} | HO VA TEN: {self.name} | LOAI: {self.get_loai()} ")
    def display_salaries(self):
        print(f"MA NV : {self.employee_id} | HO VA TEN: {self.name} | LUONG: {self.calculate_salary():,.0f} ")

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_loai(self):
        pass



class FullTimeEmployee(Employee):
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary=base_salary
        self.bonus=bonus


    def  calculate_salary(self):
        return self.base_salary+self.bonus

    def get_loai(self):
        return "Full-Time"


class PartTimeEmployee(Employee):

    def __init__(self, employee_id, name,working_hours,hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours=working_hours
        self.hourly_rate=hourly_rate
    def calculate_salary(self):
        return self.working_hours*self.hourly_rate
    def get_loai(self):
        return 'Part-time'


class InternEmployee(Employee):
    def __init__(self, employee_id, name,allowance):
        super().__init__(employee_id, name)
        self.allowance=allowance

    def calculate_salary(self):
        return self.allowance
    def get_loai(self):
        return 'Intern'

def salary_employee(employe):
    print("--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for i in employe:
        i.display_salaries()

def display(employee):
    for i in employee:
        i.display_info()

employees = [
    FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
    PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
    InternEmployee("E003", "Le Van C", 3000000)
]


while True:
    choose=input("""
    === EMPLOYEE SALARY MANAGER ===
    1. Xem danh sách nhân viên
    2. Tính lương toàn bộ nhân viên
    3. Thoát chương trình
    ================================
    Chọn chức năng (1-3):
    """)
    match choose:
        case "1":
            display(employees)
        case "2":
            salary_employee(employees)
