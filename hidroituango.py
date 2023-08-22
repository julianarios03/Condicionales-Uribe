nivelAgua=int(input("Cual es el nivel de agua: "))

#Evaluando multiples condiciones
if nivelAgua >0 and nivelAgua<=200:
    print(f"El nivel de agua es :{nivelAgua}, esta muy bajo")
elif nivelAgua >200 and nivelAgua<=400:
     print(f"El nivel de agua es :{nivelAgua}, estamos operando con normalidad")
elif nivelAgua>400:
     print(f"El nivel de agua es :{nivelAgua}, inicie plan de evacuacion...")
else
    print("por favor revise el sensor de agua,nivel no valido")
           