# ตอนที่ 4 - กำหนดค่าให้ Attribute

#เพิ่มชื่อเเละเงินเดือนของพนักงานเข้าไป
class Employee: #การสร้างคลาส
    #สร้างเมธอด
    def detial(self,name,salary,department):
        self.name = name #กำหนด Attribute 
        self.salary = salary #กำหนด Attribute 
        self.department = department #กำหนด Attribute 
        

    def showData(self):
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
        print("เเผนก = {}".format(self.department))
    

#การสร้างวัตถุ
obj1 = Employee()
obj1.detial("tao",5000,"mhee")

obj2 = Employee()
obj2.detial("tao2",1000,"Hacker")

obj3 = Employee()
obj3.detial("tao3",45555,"hoy")


obj1.showData()
obj2.showData()
obj3.showData()
