import random

intentosRealizados = 0

print('Hola, Como te llamas?')
miNombre = input('Introduce tu nombre: ')

numero = random.randint(1, 20)
print('Bueno ' + miNombre + ' estoy pensando en un numero entre 1 y 20.')

while intentosRealizados < 6:
    print('Intenta adivinar')
    estimacion = int(input())

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero: 
        print('Tu estimacion es muy baja.')

    if estimacion > numero:
            print('Tu estimacion es muy alta.')

    if estimacion == numero:
            break

if estimacion == numero:
    print('Buen trabajo' + miNombre + ' Has adivinado mi numero en ' + str(intentosRealizados) + ' intentos')

if estimacion != numero:

    print('Pues no. El numero que estaba pensando era ' + str(numero))
