anio = int(input("Introduzca una fecha: "))

if anio >= 1920 and anio <= 1940:
    print("Generación Silenciosa")
    
elif anio >= 1946 and anio <= 1964:
    print("Baby Boomer")

elif anio >= 1965 and anio <= 1979:
    print("Generación X")

elif anio >= 1980 and anio <= 2000:
    print("Generación Y")

elif anio >= 2001 and anio <= 2010:
    print("Generación Z")

elif anio >= 2011 and anio <= 2022:
    print("Generación Alpha")

else:
    print("No clasifica")