# ตอนที่ 13 - สร้าง Class สืบทอดคุณสมบัติ

class Employee: #การสร้างคลาส
    # class vatiable 
    minSalary = 12000
    maxSalary = 50000
    __companyName = "บริษัทxyzจำกัด"
#----------------------------------------------------------------
    def __init__ (self,name,salary,department):
        #Protected Attribute
        self.__name = name #กำหนด Attribute 
        self.__salary = salary #กำหนด Attribute 
        self._department = department #กำหนด Attribute 
    
    #Private Method
    ''' def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("เเผนก = {}".format(self.__department))  '''

    
    def _showData(self):
        print("ชื่อพนักงาน = "+self.__name)
        print("เงินเดือน = ",format(self.__salary))
        print("เเผนก = "+self._department) 

class Accounting(Employee):    #สืบทอดคุณสมบัติจาก Employee
    __departmentName = "พนักงานบัญชี"
    def __init__ (self): #default constructor
        pass
        

class Programmer(Employee):    #สืบทอดคุณสมบัติจาก Employee
    __departmentName = "พนักงานพัฒนาระบบ"
    def __init__ (self): #default constructor
        pass

class Sale(Employee):     #สืบทอดคุณสมบัติจาก Employee
    __departmentName = "พนักงานขายสินค้า"
    def __init__ (self): #default constructor
        pass
    

#การสร้างวัตถุ
account = Accounting()
print(account._Employee__companyName) #ใช้คอนสตรัทเตอร์จากเเม่ ในกรณีเเบบ private

programmer = Programmer()
print(programmer.minSalary)  #ใช้คอนสตรัทเตอร์จากเเม่
sale = Sale()



'''
obj1 = Employee("tao",5000,"mhee")


print("เงินเดือนต่ำสุดของพนักงาน = "+str(Employee._maxSalary))
print(obj1._companyName)'''