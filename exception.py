try:
    birinchi = int(input("birinchi sonni kiriting: "))
    ikkinchi = int(input("ikkinchi sonni kiriting: "))
    amal = input("amal kiriting")
    if amal == "-":
        print(birinchi-ikkinchi)
    elif amal =="+":
        print(birinchi+ikkinchi)
    elif amal == "/":
        print(birinchi/ikkinchi)
    elif amal == "*":
        print(birinchi*ikkinchi)
except ZeroDivisionError:
    print("sonni nolga bo'lib bo'lmaydi")
except:
    print("son bilan tekstda birgalikda amal bajarib bo'lmaydi")