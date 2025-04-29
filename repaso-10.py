edad = int(input("ingresa tu edad :"))
if edad < 5:
    print("niño")
elif edad >= 5 and edad < 17:
    print("adolecente")
elif edad >= 17 and edad < 49:
    print("adulto")
elif edad >= 49 and edad < 100:
    print("anciano")
else:
    print("edad no validad")
