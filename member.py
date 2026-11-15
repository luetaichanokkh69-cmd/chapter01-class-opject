class member:
    def __init__(self, name, visits, mouths, monthly_fee):
        self.name = name
        self.visits = visits
        self.mouths = mouths
        self.monthly_fee = monthly_fee
#selfคือแอตทริบิวท์และself.nameเป็นการประกาศตัวแปลนั้นในวงเล็บ 

    def is_at_risk(self):
        return self.visits < 4 and self.mouths > 6
    
    def total_paid(self):
        return self.mouths * self.monthly_fee
        
#object
m1 = member("Luetaichanok", 2, 10, 900)
m2 = member("Maria", 5, 12, 900)
m3 = member("natthapong", 3, 8, 900)
m4 = member("Kanyarat", 1, 15, 900)

print("ชื่อสมาชิก : ", m1.name)
print("จำนวนครั้งที่ใช้งาน : ", m1.visits)
print("อายุสมาชิก : ", m1.mouths ,"เดือน")
print("เสี่ยงเลิกใช้บริการ : ", m1.is_at_risk())
print("ยอดชำระทั้งหมด : ", m1.total_paid(), "บาท")
print()

print("ชื่อสมาชิก : ", m2.name)
print("จำนวนครั้งที่ใช้งาน : ", m2.visits)    
print("อายุสมาชิก : ", m2.mouths ,"เดือน")
print("เสี่ยงเลิกใช้บริการ : ", m2.is_at_risk())
print("ยอดชำระทั้งหมด : ", m2.total_paid(), "บาท")
print()

print("ชื่อสมาชิก : ", m3.name)
print("จำนวนครั้งที่ใช้งาน : ", m3.visits)    
print("อายุสมาชิก : ", m3.mouths ,"เดือน")
print("เสี่ยงเลิกใช้บริการ : ", m3.is_at_risk())
print("ยอดชำระทั้งหมด : ", m3.total_paid(), "บาท")
print()

print("ชื่อสมาชิก : ", m4.name)
print("จำนวนครั้งที่ใช้งาน : ", m4.visits)    
print("อายุสมาชิก : ", m4.mouths ,"เดือน") 
print("เสี่ยงเลิกใช้บริการ : ", m4.is_at_risk())
print("ยอดชำระทั้งหมด : ", m4.total_paid(), "บาท")
