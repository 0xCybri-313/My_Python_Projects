class Company:
    company = "Apple"

    def __init__(self):
        print(self.company)

    def detail(self):
        self.total_emp = "786"
        self.location = "unknown"
        self.total_rev = "1 Trillion"

    def show(self):
        print(f"Company Name   :   \n\nEmpolee Numbers\n\nEmpolee Name  :   \n\nLocation     :   \n\nCompany Ravenue  :   ")
        print(f"Company Name   :   {Company.company}\n\nEmpolee Numbers\n\nEmpolee Name  :   {self.total_emp}\n\nLocation     :   {self.location}\n\nCompany Ravenue  :   {self.total_rev}")

class Empolee(Company):

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def salary(self, id):
        if len(id) == 2:
            self.salary = "2500 $"
        else:
            self.salary = "1000 $"

    def show(self):

        print(f"Company Name   :   {Empolee.company}\n\nEmpolee Detail\n\nEmpolee Name   :   {self.name}\n\nEmpolee ID     :   {self.id}\n\nEmpolee Salay  :   ****")

    def com_detail(self):
        super().show()

emp1 = Empolee("Raju", 123)
emp1.show()
emp1.com_detail(self)