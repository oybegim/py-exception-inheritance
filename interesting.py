import time
ism = input("ismingizni kiriting")
familiya = input("familiyangizni kiriting")
parol = int(input("parol kiriting"))
login = input("login kiriting")
if parol == 1234 and login == "login1234":
    print("parol va login to'g'ri")
elif parol != 1234 and login == "login1234":
    print("parol xato 4 sekund kuting")
    time.sleep(4)
    print("4 sekund o'tdi")
elif parol == 1234 and parol != "login1234":
    print("login xato 4 sekund kuting")
    time.sleep(4)
    print("4 sekund o'tdi")
elif parol != 1234 and login != "login1234":
    print("parol va login xato 4 sekund kuting")
    time.sleep(4)
    print("4 sekund o'tdi")
ozgaruvchi = int(input("raqamlardan birini tanlang: 1.Kalkulyator va 2.Class"))
if ozgaruvchi == 1:
    birinchi = int(input("birinchi sonni kiriting"))
    ikkinchi = int(input("ikkinchi sonni kiriting"))
    amal = input("amalni kiriting")
    if amal == "-":
        print(birinchi - ikkinchi)
    elif amal == "+":
        print(birinchi+ikkinchi)
    elif amal == "/":
        print(birinchi/ikkinchi)
    elif amal == "*":
        print(birinchi*ikkinchi)
elif ozgaruvchi == 2:
    class Odam:
        def __init__(self, ismi, familiyasi, yoshi, kasbi):
            self.ismi = ismi
            self.familiyasi = familiyasi
            self.yoshi = yoshi
            self.kasbi = kasbi
odam1 = Odam("Mustafo", "Amirbekov", 26, "Diplamatiya")
odam2 = Odam("Amirbek", "Mustafoyev", 28, "Dasturchi")
print(odam1.ismi, odam1.familiyasi, odam1.yoshi, odam1.kasbi)
print(odam2.ismi, odam2.familiyasi, odam2.yoshi, odam2.kasbi)