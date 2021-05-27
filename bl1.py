from machine import UART, Pin
import time

uartNico = UART(0,9600) # Creación de un objeto con la función UART incluida en las librerías 
led_adelante = Pin(12,Pin.OUT) # configuración de pines como salidas
led_izquierda = Pin(13,Pin.OUT) # configuración de pines como salidas
led_derecha = Pin(14,Pin.OUT) # configuración de pines como salidas
led_reversa = Pin(15,Pin.OUT) # configuración de pines como salidas

while true:
    dato = uartNico.read(1) # Lee lo que se ecuentra en el puerto y el 1 es para que lo haga caracter por caracter
    led_adelante.value(0) # Apagamos led
    led_izquierda.value(0) # Apagamos led
    led_derecha.value(0) # Apagamos led
    led_reversa.value(0) # Apagamos led
    
    if "a" in dato: # Encendemos la únicamente la letra que va llegando
        led_adelante.value(1)
    if "b" in dato: # Encendemos la únicamente la letra que va llegando
        led_izquierda.value(1)
    if "d" in dato: # Encendemos la únicamente la letra que va llegando
         led_derecha.value(1)
    if "e" in dato: # Encendemos la únicamente la letra que va llegando
       led_reversa.value(1)
    print(dato)
    time.sleep(0.5)
    
    