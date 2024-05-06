
from pycreate2 import Create2
import keyboard  # Librería para detectar las teclas presionadas

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

# Crear una instancia de Create2 y establecer la conexión
port = "COM5"  # Puerto serial donde está conectado el Roomba
bot = Create2(port)
bot.start()
bot.safe()

# Bucle para detectar las teclas presionadas y controlar el Roomba
keyboard.hook(controlar_roomba)
keyboard.wait('esc')  # Esperar hasta que se presione la tecla 'Esc' para detener el programa

# Cerrar la conexión al finalizar
bot.drive_stop()





bot.close()