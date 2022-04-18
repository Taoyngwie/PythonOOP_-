#ตอนที่ 3 - การสร้าง Attribute และ Method

#เพิ่มชื่อเเละเงินเดือนของพนักงานเข้าไป
class Employee: #การสร้างคลาส
    #สร้างเมธอด
    def detial(self):
        self.name = "เต่าอิงวี่" #กำหนด Attribute 
        self.salary = 10000 #กำหนด Attribute 
        print("ชื่อพนักงาน = {}".format(self.name))
        print("เงินเดือน = {}".format(self.salary))
    

#การสร้างวัตถุ
emp1 = Employee()
emp1.detial()
