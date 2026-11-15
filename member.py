class member:
    def __init__(self, name, visits, mouths):
        self.name = name
        self.visits = visits
        self.mouths = mouths
#selfคือแอตทริบิวท์และself.nameเป็นการประกาศตัวแปลนั้นในวงเล็บ 

    def is_at_risk(self):
        return self.visits < 4 and self.mouths > 6

#object
m1 = member("Luetaichanok", 2, 10)
m2 = member("Nattapong", 5, 12)
m3 = member("Pimchanok", 3, 8)
m4 = member("kanyarat", 1, 15)

print("ชื่อสมาชิก : ", m1.name)
print("จำนวนครั้งที่ใช้งาน : ", m1.visits)
print("อายุสมาชิก : ", m1.mouths ,"เดือน")
print("เสี่ยงเลิกใช้บริการ : ", m1.is_at_risk())
print()

print("ชื่อสมาชิก : ", m2.name)
print("จำนวนครั้งที่ใช้งาน : ", m2.visits)    
print("อายุสมาชิก : ", m2.mouths ,"เดือน")
print("เสี่ยงเลิกใช้บริการ : ", m2.is_at_risk())
print()

print("ชื่อสมาชิก : ", m3.name)
print("จำนวนครั้งที่ใช้งาน : ", m3.visits)    
print("อายุสมาชิก : ", m3.mouths ,"เดือน")
print("เสี่ยงเลิกใช้บริการ : ", m3.is_at_risk())
print()

print("ชื่อสมาชิก : ", m4.name)
print("จำนวนครั้งที่ใช้งาน : ", m4.visits)    
print("อายุสมาชิก : ", m4.mouths ,"เดือน") 
print("เสี่ยงเลิกใช้บริการ : ", m4.is_at_risk())
