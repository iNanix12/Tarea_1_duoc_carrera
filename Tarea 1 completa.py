print("¡Comienza la carrera!")
print(" 1-Si \n 2-No")

#Esta línea de código sirve para contrarestar el True con los false
opcion1 = True
while opcion1: 
    valla = str(input("¿Haz encontrado una valla? (Elige opción 1 o 2): "))
    if valla == "1":
        print("Salta la valla ")
        opcion1=False
    elif valla == "2":
        print("Siga corriendo")
        opcion1=False
    else:
        print("Selecciona opción 1 o 2")

#Esta línea de codigo es diferente a la primera en cuanto a romper el bucle
while True: 
    print("¡Segundo obtáculo!")
    tunel = str(input("¿Has encontrado un túnel?: \n 1- Si \n 2- No: \n " ))
    if tunel == "1":
        print("Atraviesa el túnel")
        break
    elif tunel == "2":
        print("Siga corriendo")
        break
    else:
        print("Selecciona opción 1 o 2")
    


opcion3 = True
while opcion3:
    print("¡Tercer obstáculo!")
    laguna = str(input("¿Has encontrado una laguna?: \n 1- Si \n 2- No: \n"))
    if laguna == "1":
        print("Intentaste nadar, pero te has agotado a medio camino y por ende, te devuelves perdiendo la carrera")
        opcion3 = False
    elif laguna == "2":
        print("¡Has ganado la carrera! \n ¡Felicitaciones!")
        opcion3 = False
    else:
        print("Selecciona opción 1 o 2")


print("Finaliza el programa")


    