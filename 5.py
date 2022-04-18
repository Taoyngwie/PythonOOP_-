# ตอนที่ 6 - ฟังก์ชั่นเกี่ยวกับ Class & Object


class Employee: #การสร้างคลาส
    #Constructer
    '''def __init__ (self):
        print("ทดสอบคอนสตรัทเตอร์") '''
        
    #ใช้งาน Constructer ในการกำหนดค่าเเบบอัตโนมัติได้เลย 
    def __init__ (self,name,salary,department):
        self.name = name #กำหนด Attribute 
        self.salary = salary #กำหนด Attribute 
        self.department = department #กำหนด Attribute 
    
    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("เเผนก = {}".format(self.department))
    
    '''def __del__ (self):
        print("call Destructer")'''
    

#การสร้างวัตถุ
obj1 = Employee("tao",5000,"mhee")

obj2 = Employee("tao2",1000,"Hacker")

obj3 = Employee("tao3",45555,"hoy")


#สร้างงานฟังก์ชันที่เกี่ยวข้อง

#isinstance = คอยตรวจสอบว่าเป็น เป็น instance ของ class นั้นหรือไม่
print(isinstance(obj1,Employee))

#เเสดง Attribute and Method ของ  instance ตัวนั้น
print(dir(obj1))

#เเสดงชื่อ class ของ obj
print(obj1.__class__)
