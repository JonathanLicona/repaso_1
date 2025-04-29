nota = int(input("ingresa tun nota:"))
if nota < 5:
    print("perdio")
elif nota >= 5 and nota < 7:
    print("aprobado")
elif nota >= 7 and nota <= 10:
    print("sobresaliente")
else:
    print("no invalida")
