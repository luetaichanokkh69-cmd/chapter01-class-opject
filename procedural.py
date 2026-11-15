name="Luetaichanok"
visits=2
mouths=10

#ฟังชันก์สำหรับตรวจสอบความเสี่ยง
def is_at_risk(visits, mouths):
    return visits < 4 and mouths > 6

#แสดงผลลัพธ์
print("ชื่อสมาชิก : ", name)
print("จำนวนครั้งที่ใช้งาน : ", visits)
print("อายุสมาชิก : ", mouths ,"เดือน")
print("เสี่ยงเลิกใช้บรการ : ", is_at_risk(visits, mouths))
