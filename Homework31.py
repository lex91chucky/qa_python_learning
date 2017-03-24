class worker:
    def __init__(self, fio):
        #, position, salary, work_experience):
        self.fio = fio
#        self.position = position
#        self.salary = salary
#        self.work_experience = work_experience
    def name(self, fio):
        a = self.fio.split()
        return a[0]
    def lastname(self, fio):
        b = self.fio.split()
        return b[1]
    def salary(self, month, permonth):
        self.month = month
        self.permonth = permonth
        b = month * permonth
        b = str(b)
        h = "Salary = " + b + "$"
        return h
    def position(self, month):
        self.month = month
        if 0 <= month < 36:
            c = "Junior"
        elif 72 >= month >= 36:
            c = "Middle"
        elif month > 72:
            c = "Senior"
        else: c = "Not valid value"
        return c
if __name__=="__main__":
    c = worker("Alex Korchak")
    b = c.name("Alex Korchak")
    v = c.lastname("Alex Korchak")
    n = c.salary(3, 1400)
    f = c.position(44)
    print(b)
    print(v)
    print(n)
    print(f)