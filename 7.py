# ตอนที่ 10 - Getter , Setter Method


from hashlib import new


class Employee: #การสร้างคลาส
    #Constructer
    '''def __init__ (self):
        print("ทดสอบคอนสตรัทเตอร์") '''

#----------------------------------------------------------------
   #ใช้งาน Constructer ในการกำหนดค่าเเบบอัตโนมัติได้เลย (Public)
    '''def __init__ (self,name,salary,department):
        #public Attribute
        self.name = name #กำหนด Attribute 
        self.salary = salary #กำหนด Attribute 
        self.department = department #กำหนด Attribute 
    
    #public Method
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("เเผนก = {}".format(self.department)) '''
#----------------------------------------------------------------
    #ใช้งาน Constructer ในการกำหนดค่าเเบบอัตโนมัติได้เลย (Protected)
    '''def __init__ (self,name,salary,department):
        #Protected Attribute
        self._name = name #กำหนด Attribute 
        self._salary = salary #กำหนด Attribute 
        self._department = department #กำหนด Attribute 
    
    #Protected Method
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self._name))
        print("เงินเดือน = {}".format(self._salary))
        print("เเผนก = {}".format(self._department)) '''

#----------------------------------------------------------------
    #ใช้งาน Constructer ในการกำหนดค่าเเบบอัตโนมัติได้เลย (Private)
    def __init__ (self,name,salary,department):
        #Protected Attribute
        self.__name = name #กำหนด Attribute 
        self.__salary = salary #กำหนด Attribute 
        self.__department = department #กำหนด Attribute 
    
    #Private Method
    ''' def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("เเผนก = {}".format(self.__department))  '''


    #หรือนำไปเขียนได้อีกเเบบ
     #Private Method
    def _showData(self):
        print("ชื่อพนักงาน = "+self.getName())
        print("เงินเดือน = ",format(self.getSalary()))
        print("เเผนก = "+self.getDepartment()) 
    

#----------------------------------------------------------------
    #ปรับค่าตัวเเปรในเมธอด(setter)
    def setName(self,newname):
        self.__name = newname

    def setSalary(self,newsalary):
        self.__salary = newsalary
    
    def setDepartment(self,newdepartment):
        self.__department = newdepartment
#-----------------------------------------------------------------
    #รับค่าจากตัวเเปรในเมธอด(getter)
    
    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

#------------------------------------------------------------------

#การสร้างวัตถุ
obj1 = Employee("tao",5000,"mhee")
obj2 = Employee("tao2",1000,"Hacker")
obj3 = Employee("tao3",45555,"hoy")

#------------------------------------------------------------------
#การเข้าถึงข้อมูลของ Private
#เดียวใช้ set/get

'''
obj1.setName("hee")
print("เเสดงผลชื่อพนักงาน {}".format(obj1.getName()))
obj1.setSalary(5)
print("เเสดงผลชื่อพนักงาน {}".format(obj1.getSalary()))
obj1.setDepartment("prog")
print("เเสดงผลชื่อพนักงาน {}".format(obj1.getDepartment())) '''
#------------------------------------------------------------------
#เขียนเเบบเรียกใช้งานเป็นเมธอด
"""
obj1._showData()
#ถ้าใช้เมธอดในฝั่งนี้สามารถเอาตัว getter / setter ออกได้เลย
"""

#ถ้าจะเข้าถึงจากนอกคล้าสไดเทุกตัวยกเว้น private