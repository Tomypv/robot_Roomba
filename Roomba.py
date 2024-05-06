
from pycreate2 import Create2
import keyboard  # Librería para detectar las teclas presionadas
import random
import time

# Función para controlar el movimiento del Roomba
def controlar_roomba(tecla):
    if tecla.name == 'up' or tecla.name == 'w':
        bot.drive_direct(100, 100)  # Avanzar
        sensor = bot.get_sensors()
        print(sensor)
    elif tecla.name == 'down' or tecla.name == 's':
        bot.drive_direct(-100, -100)  # Retroceder
        sensor = bot.get_sensors()
        print(sensor)
    elif tecla.name == 'left' or tecla.name == 'a':
        bot.drive_direct(-100, 100)  # Girar a la izquierda
        sensor = bot.get_sensors()
        print(sensor)
    elif tecla.name == 'right' or tecla.name == 'd':
        bot.drive_direct(100, -100)  # Girar a la derecha
        sensor = bot.get_sensors()
        print(sensor)
    else:
        bot.drive_stop()  # Detener el movimiento si no se presiona ninguna tecla de movimiento

def movimiento_aleatorio():
    while True:
        # Generar velocidades aleatorias para cada rueda
        velocidad_izquierda = random.randint(-500, 500)
        velocidad_derecha = random.randint(-500, 500)
        bot.drive_direct(velocidad_izquierda, velocidad_derecha)
        time.sleep(0.5)  # Pausa breve para permitir el movimiento

        # Detener el movimiento si se presiona otra tecla
        if keyboard.is_pressed('q'):  # Puedes cambiar 'q' por cualquier tecla para detener
            bot.drive_stop()
            break

# Crear una instancia de Create2 y establecer la conexión
port = "COM5"  # Puerto serial donde está conectado el Roomba
bot = Create2(port)
bot.start()
bot.safe()

# Bucle para detectar las teclas presionadas y controlar el Roomba
keyboard.add_hotkey('r', movimiento_aleatorio)
keyboard.hook(controlar_roomba)
keyboard.wait('esc')  # Esperar hasta que se presione la tecla 'Esc' para detener el programa

# Cerrar la conexión al finalizar
bot.drive_stop()
bot.close()