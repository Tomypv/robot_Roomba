
import math
from pycreate2 import Create2
from pynput import keyboard as kb
import random
import time
#Especificaciones del Robot

ANCHO = 5
LARGO = 5
EJE_RUEDAS = 235 #Es en milimetros
DIAM_RUEDAS = 72 #Es en milimetros
RESOL_ENCODER = 508.8
RELA_REDUCCION = 1
CUARTO_CIRCUN = 1750/2
pos_anterior_x = 0
pos_anterior_y = 0
giro_anterior = 0

def calularConversion():
    conversion = (2*math.pi * (DIAM_RUEDAS/2)) / (RELA_REDUCCION*RESOL_ENCODER)
    
    return conversion



##Mover Robot Calculando la odometria y posicion en ese momento del robot

def pulsa(tecla):
    global pos_anterior_x
    global pos_anterior_y
    global giro_anterior
    historico_der = []
    historico_izq = []



    if (tecla == kb.KeyCode.from_char('w')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(100, 100)

        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(Encoder_der_Act)
        historico_izq.append(Encoder_izq_Act)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der - Desplazamiento_izq) / 2

        Giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+Giro)
        inc_y = avance_promedio * math.sin(giro_anterior+Giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

        if giro_anterior > 2*math.pi:
            giro_anterior = 0
        if giro_anterior <= (-2*math.pi):
            giro_anterior = 0

        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('GIRO: ' + str(giro_anterior))

    elif (tecla == kb.KeyCode.from_char('s')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(-100, -100)

        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(Encoder_der_Act)
        historico_izq.append(Encoder_izq_Act)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der - Desplazamiento_izq) / 2

        Giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+Giro)
        inc_y = avance_promedio * math.sin(giro_anterior+Giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

        if giro_anterior > 2*math.pi:
            giro_anterior = 0
        if giro_anterior <= (-2*math.pi):
            giro_anterior = 0

        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('GIRO: ' + str(giro_anterior))

    elif (tecla == kb.KeyCode.from_char('d')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(100, -100)

        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(Encoder_der_Act)
        historico_izq.append(Encoder_izq_Act)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der - Desplazamiento_izq) / 2

        Giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+Giro)
        inc_y = avance_promedio * math.sin(giro_anterior+Giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

        if giro_anterior > 2*math.pi:
            giro_anterior = 0
        if giro_anterior <= (-2*math.pi):
            giro_anterior = 0

        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('GIRO: ' + str(giro_anterior))

    elif (tecla == kb.KeyCode.from_char('a')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(-100, 100)

        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(Encoder_der_Act)
        historico_izq.append(Encoder_izq_Act)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der - Desplazamiento_izq) / 2

        Giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+Giro)
        inc_y = avance_promedio * math.sin(giro_anterior+Giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

        if giro_anterior > 2*math.pi:
            giro_anterior = 0
        if giro_anterior <= (-2*math.pi):
            giro_anterior = 0

        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('GIRO: ' + str(giro_anterior))

    elif (tecla == kb.KeyCode.from_char('e')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(100, 50)

        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(Encoder_der_Act)
        historico_izq.append(Encoder_izq_Act)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der - Desplazamiento_izq) / 2

        Giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+Giro)
        inc_y = avance_promedio * math.sin(giro_anterior+Giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

        if giro_anterior > 2*math.pi:
            giro_anterior = 0
        if giro_anterior <= (-2*math.pi):
            giro_anterior = 0

        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('GIRO: ' + str(giro_anterior))
        
    elif (tecla == kb.KeyCode.from_char('q')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(50, 100)

        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(Encoder_der_Act)
        historico_izq.append(Encoder_izq_Act)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der - Desplazamiento_izq) / 2

        Giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+Giro)
        inc_y = avance_promedio * math.sin(giro_anterior+Giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

 

        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('GIRO: ' + str(giro_anterior))

    
    elif (tecla == kb.KeyCode.from_char('p')):
        print('salir tontin: ' + str(tecla))
        exit()
    elif (tecla == kb.KeyCode.from_char('r')):
        movimiento_aleatorio()
        exit()
    else:
        print('Tecla invalida like your mom')
    
    # Limpiar pantalla





def movimiento_aleatorio():
    while True:
        #Calcular posicion del los encoders-TODO

        # Generar velocidades aleatorias para cada rueda
        velocidad_izquierda = random.randint(-500, 500)
        velocidad_derecha = random.randint(-500, 500)
        bot.drive_direct(velocidad_izquierda, velocidad_derecha)
        time.sleep(0.5)  # Pausa breve para permitir el movimiento
        #Recalcular posicion de los encoders y guardar movimiento de encoder en los arrays-TODO
        
        #Calculos de odometria-TODO
        # Detener el movimiento si se presiona otra tecla
        if kb.is_pressed('q'):  # Puedes cambiar 'q' por cualquier tecla para detener
            bot.drive_stop()
            break

def vuelta_a_casa(historico_izq, historico_der):

    if len(historico_izq) != len(historico_der):
        raise ValueError("Los arrays deben tener la misma longitud")

    longitud = len(historico_izq)
    for i in range(longitud - 1, -1, -1):
        bot.drive_direct(-historico_izq[i], -historico_der[i])




# Crear una instancia de Create2 y establecer la conexión
port = "COM6"  # Puerto serial donde está conectado el Roomba
bot = Create2(port)
bot.start()
bot.safe()

# Bucle para detectar las teclas presionadas y controlar el Roomba
conversion = calularConversion()
print('Conversion anal: ' + str(conversion))
with kb.Listener(pulsa) as escuchador:
    escuchador.join()    # Esperar hasta que se presione la tecla 'Esc' para detener el programa

# Cerrar la conexión al finalizar
bot.drive_stop()
bot.close()