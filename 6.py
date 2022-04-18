# ตอนที่ 7 - การห่อหุ้ม (Encapsulation)


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
    
    #Protected Method
    def _showData(self):
        print("ชื่อพนักงาน = {}".format(self.__name))
        print("เงินเดือน = {}".format(self.__salary))
        print("เเผนก = {}".format(self.__department)) 

#----------------------------------------------------------------
    
    '''def __del__ (self):
        print("call Destructer")'''
    

#การสร้างวัตถุ
obj1 = Employee("tao",5000,"mhee")
obj2 = Employee("tao2",1000,"Hacker")
obj3 = Employee("tao3",45555,"hoy")



#การเข้าถึงข้อมูลของ Public
''' 
obj1.name = "hee"
obj1.showData()
'''
#การเข้าถึงข้อมูลของ Protected
'''obj1._name = "hee"
obj1._showData() '''

#การเข้าถึงข้อมูลของ Private
#เดียวใช้ set/get