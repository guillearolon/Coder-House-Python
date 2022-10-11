peso_user = float(input("¿Cuál es su peso? [Kg]: "))
altura_user = float(input("¿Cuál es su altura? [Mts]: "))

imc = peso_user / (altura_user ** 2)

print("Indice de masa corporal es: ",round(imc))