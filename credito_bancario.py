edad = int(input("¿Cuál es su edad? "))
           
antiguedad = int(input("¿Cuál es su antiguedad financiera? "))
                 
ingreso = int(input("¿Cuál es su ingreso mensual en dolares? "))
              
if edad >= 18:
                if antiguedad >= 3 and ingreso >= 2500:
                  print("Aprobado")
                  

                elif ingreso >= 4000:
                    print("Aprobado")
    
                else:
                    print("No aprobado")
    
else:
    print("No aprobado")