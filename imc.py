personas = int(input( "Personas: "))
while personas > 0:
    nombre = input("Su nombre: ")
    paterno =input("Apellido paterno: ")
    materno =input("Apellido materno: ")
    edad = int(input("Edad: "))
    peso =float(input("Su peso en Kg: "))
    altura =float(input("Su altura en mts: "))
    IMC = (peso / altura**2)

    if(edad < 18):
        print("Menor de edad")
    else:
        print("Mayor de edad")

    print ("IMC: " + str(IMC))

    if IMC >= 0 and IMC <= 18.99 :
        print ("Peso bajo")
    elif IMC >= 18.50 and IMC <= 24.99 :
        print ("Peso normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print ("Sobre peso")
    elif IMC >= 30.00 and IMC <= 34.99 :
        print ("Obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.99:
        print ("Obesidad media")
    elif IMC > 40.00:
        print ("Obesidad morbida")