from machine import UART
uartNico = UART(0,9600) # Creación de un objeto con la función UART incluida en las librerías 
while True:
    dato = uartNico.read(1) # Lee lo que se ecuentra en el puerto y el 1 es para que lo haga caracter por caracter
    print(dato)