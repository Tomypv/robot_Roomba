
import math
from pycreate2 import Create2
from pynput import keyboard as kb
import random
import pygame
import time
#Especificaciones del Robot

ANCHO = 50
LARGO = 50
EJE_RUEDAS = 23.5 #Es en milimetros
DIAM_RUEDAS = 7.2 #Es en milimetros
RESOL_ENCODER = 508.8
RELA_REDUCCION = 1
pos_anterior_x = 0
pos_anterior_y = 0
historico_der = []
historico_izq = []
rastro = []
giro_anterior = 0
i = 1.0  # Inicializar i a 1.0 (velocidad normal)
pygame.init()
# Definir dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mapa del Robot")

# Función para dibujar el mapa
def dibujar_mapa(x, y, rastro):
    screen.fill(NEGRO)  # Limpiar pantalla
    pygame.draw.rect(screen, BLANCO, (x, y, ANCHO, LARGO))  # Dibujar robot (rectángulo)
    for punto in rastro:
        pygame.draw.rect(screen, ROJO, (punto[0], punto[1], 2, 2))  # Dibujar rastro del robot

    mostrar_texto("X: " + str(pos_anterior_x), 600, 0)
    mostrar_texto("Y: " + str(pos_anterior_y), 600, 20)
    mostrar_texto("ÁNGULO: " + str(giro_anterior*(180/math.pi)), 600, 40)
    pygame.display.flip()  # Actualizar pantalla
def calularConversion():
    conversion = (2*math.pi * (DIAM_RUEDAS/2)) / (RELA_REDUCCION*RESOL_ENCODER)
    
    return conversion

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

##Mover Robot Calculando la odometria y posicion en ese momento del robot

def pulsa(tecla, i):
    global pos_anterior_x
    global pos_anterior_y
    global giro_anterior



    if (tecla == kb.KeyCode.from_char('w')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(100*i, 100*i)
        time.sleep(1)
        bot.drive_stop()
        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(100*i)
        historico_izq.append(100*i)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2
        print('Avance derecho' + str(Desplazamiento_der))
        print('Avance izquierdo' + str(Desplazamiento_izq))
        print('Avance: ' + str(avance_promedio))
        giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+giro)
        inc_y = avance_promedio * math.sin(giro_anterior+giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y
        giro_anterior += giro
        if giro_anterior > 2*math.pi:
            giro_anterior = giro_anterior - 360
        if giro_anterior <= (-2*math.pi):
            giro_anterior = giro_anterior + 360
        

            # Actualizar rastro
        rastro.append((pos_anterior_x, pos_anterior_y))

            # Dibujar mapa
        dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro)

        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('giro: ' + str(giro_anterior))


    elif (tecla == kb.KeyCode.from_char('s')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(-100*i, -100*i)
        time.sleep(1)
        bot.drive_stop()
        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(-100*i)
        historico_izq.append(-100*i)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2


        giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+giro)
        inc_y = avance_promedio * math.sin(giro_anterior+giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y
        giro_anterior += giro
        if giro_anterior > 2*math.pi:
            giro_anterior = giro_anterior - 360
        if giro_anterior <= (-2*math.pi):
            giro_anterior = giro_anterior + 360
        

            # Actualizar rastro
        rastro.append((pos_anterior_x, pos_anterior_y))
            # Dibujar mapa
        dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro)
        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('giro: ' + str(giro_anterior))

    elif (tecla == kb.KeyCode.from_char('d')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(100*i, -100*i)
        time.sleep(1)
        bot.drive_stop()
        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(-100*i)
        historico_izq.append(100*i)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2


        giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+giro)
        inc_y = avance_promedio * math.sin(giro_anterior+giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y
        giro_anterior = giro + giro_anterior
        if giro_anterior > 2*math.pi:
            giro_anterior = giro_anterior - 2*math.pi
        if giro_anterior <= (-2*math.pi):
            giro_anterior = giro_anterior + 2*math.pi
        
        rastro.append((pos_anterior_x, pos_anterior_y))
            # Dibujar mapa
        dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro)
        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('giro: ' + str(giro_anterior))

    elif (tecla == kb.KeyCode.from_char('a')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(-100*i, 100*i)
        time.sleep(1)
        bot.drive_stop()
        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(100*i)
        historico_izq.append(-100*i)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2


        giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+giro)
        inc_y = avance_promedio * math.sin(giro_anterior+giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y
        giro_anterior = giro + giro_anterior 
        if giro_anterior > 2*math.pi:
            giro_anterior = giro_anterior - 2*math.pi
        if giro_anterior <= (-2*math.pi):
            giro_anterior = giro_anterior + 2*math.pi

        rastro.append((pos_anterior_x, pos_anterior_y))
            # Dibujar mapa
        dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro)   
        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('giro: ' + str(giro_anterior))

    elif (tecla == kb.KeyCode.from_char('e')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(100*i, 50*i)
        time.sleep(1)
        bot.drive_stop()
        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(50*i)
        historico_izq.append(100*i)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2


        giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+giro)
        inc_y = avance_promedio * math.sin(giro_anterior+giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

        if giro_anterior > 2*math.pi:
            giro_anterior = giro_anterior - 360
        if giro_anterior <= (-2*math.pi):
            giro_anterior = giro_anterior + 360

        rastro.append((pos_anterior_x, pos_anterior_y))
            # Dibujar mapa
        dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro) 
        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('giro: ' + str(giro_anterior))
        
    elif (tecla == kb.KeyCode.from_char('q')):
        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right

        #Mover robot

        bot.drive_direct(50*i, 100*i)
        time.sleep(1)
        bot.drive_stop()
        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        #Movimiento que ha realizado el robot

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(100*i)
        historico_izq.append(50*i)

        #Calculos de odometria

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2


        giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+giro)
        inc_y = avance_promedio * math.sin(giro_anterior+giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

        giro_anterior = giro + giro_anterior
        rastro.append((pos_anterior_x, pos_anterior_y))
            # Dibujar mapa
        dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro) 
        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('giro: ' + str(giro_anterior))

    # Manejar cambio de velocidad
    elif tecla == kb.KeyCode.from_char('n'):
        i = max(0.25, i - 0.25)  # Disminuir i en 0.25, con un mínimo de 0.25
    elif tecla == kb.KeyCode.from_char('m'):
        i = min(4.0, i + 0.25)  # Aumentar i en 0.25, con un máximo de 4.0

    
    elif (tecla == kb.KeyCode.from_char('p')):
        print('salir: ' + str(tecla))
        exit()
    elif (tecla == kb.KeyCode.from_char('r')):
        movimiento_aleatorio(tecla)
        exit()

    elif (tecla == kb.KeyCode.from_char('f')):
        busca_perimetro()
    elif (tecla == kb.KeyCode.from_char('h')):
        vuelta_a_casa(historico_izq,historico_der)
    else:
        print('Tecla invalida ')
    
    # Limpiar pantalla





def movimiento_aleatorio():
    start_time = time.time()  # Guarda el tiempo de inicio
    while time.time() - start_time < 5:  # Ejecuta el bucle mientras no se superen los 5 segundos
        # Calcular posición de los encoders - TODO

        # Generar velocidades aleatorias para cada rueda
        velocidad_izquierda = random.randint(-500, 500)
        velocidad_derecha = random.randint(-500, 500)
        bot.drive_direct(velocidad_izquierda, velocidad_derecha)
        time.sleep(0.2)  # Pausa breve para permitir el movimiento

        # Recalcular posición de los encoders y guardar movimiento de encoder en los arrays - TODO
        
        # Cálculos de odometría - TODO

def vuelta_a_casa(historico_izq, historico_der):
    print('VUELTA A CASA')
    if len(historico_izq) != len(historico_der):
        print('Los arrays deben tener la misma longitud')

    longitud = len(historico_izq)
    print('Longitud' + str(longitud))
    for i in range(longitud):
        print('Iteracion' + str(i))
        bot.drive_direct(-historico_izq[i], -historico_der[i])
        time.sleep(1)
    bot.stop()



def busca_perimetro():

    choque_frontal = False
    choque_der = False
    choque_izq = False
    choque_frontal_der = False
    choque_frontal_izq = False
    giro_anterior=0
    pos_anterior_x=0
    pos_anterior_y=0
    primera_pared = False

    historico_der = []
    historico_izq = []
    rastro = []

    
    # Bucle principal, no se cuando parar, estaría bien cuando haya recorrido todo el perímetro y llegue a la posición del primer choque -> datos_inicio
    # Hasta que posicion sea datos_inicio???
    while True:

        datos= bot.get_sensors()
        Encoder_izq = datos.encoder_counts_left
        Encoder_der = datos.encoder_counts_right
        # Movimiento hacia adelante
        bot.drive_direct(100, 100)
        # Espera de medio segundo
        time.sleep(0.2)

        # Obtener los datos de los sensores
        datos= bot.get_sensors()
        Encoder_izq_Act = datos.encoder_counts_left
        Encoder_der_Act = datos.encoder_counts_right

        Encoder_der_Act = Encoder_der_Act - Encoder_der
        Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
        historico_der.append(100)  
        historico_izq.append(100)  

        Desplazamiento_der = Encoder_der_Act * conversion
        Desplazamiento_izq = Encoder_izq_Act * conversion

        avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2


        giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

        inc_x = avance_promedio * math.cos(giro_anterior+giro)
        inc_y = avance_promedio * math.sin(giro_anterior+giro)
        pos_anterior_x = inc_x + pos_anterior_x
        pos_anterior_y = inc_y + pos_anterior_y

        if giro_anterior > 2*math.pi:
            giro_anterior = giro_anterior - 360
        if giro_anterior <= (-2*math.pi):
            giro_anterior = giro_anterior + 360
        giro_anterior = giro + giro_anterior
        rastro.append((pos_anterior_x, pos_anterior_y))
       
        # time.sleep(1)      Esto lo colocamos mañana
        # bot.drive_stop()   Esto lo colocamos mañana
            # Dibujar mapa
        dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro) 
        print('X: ' + str(pos_anterior_x))
        print('Y: ' + str(pos_anterior_y))
        print('giro: ' + str(giro_anterior))

        # Actualizar los valores de los sensores de choque
        choque_frontal = datos.wall
        choque_der = datos.cliff_right
        choque_izq = datos.cliff_left
        choque_frontal_der = datos.bumps_wheeldrops[1]
        choque_frontal_izq = datos.bumps_wheeldrops[0]

        # Obtener los datos de los sensores
        luz_der = datos.light_bumper_right
        luz_frontal_der = datos.light_bumper_front_right

        
        # Detectar colisión
        if choque_frontal or choque_der or choque_izq or choque_frontal_der or choque_frontal_izq:  

            datos= bot.get_sensors()
            Encoder_izq = datos.encoder_counts_left
            Encoder_der = datos.encoder_counts_right

            # Retrocede
            bot.drive_direct(-100, -100)
            time.sleep(0.2)

            # Obtener los datos de los sensores
            datos= bot.get_sensors()
            Encoder_izq_Act = datos.encoder_counts_left
            Encoder_der_Act = datos.encoder_counts_right

            Encoder_der_Act = Encoder_der_Act - Encoder_der
            Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
            historico_der.append(-100)  
            historico_izq.append(-100)  

            Desplazamiento_der = Encoder_der_Act * conversion
            Desplazamiento_izq = Encoder_izq_Act * conversion

            avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2


            giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

            inc_x = avance_promedio * math.cos(giro_anterior+giro)
            inc_y = avance_promedio * math.sin(giro_anterior+giro)
            pos_anterior_x = inc_x + pos_anterior_x
            pos_anterior_y = inc_y + pos_anterior_y

            if giro_anterior > 2*math.pi:
                giro_anterior = 0
            if giro_anterior <= (-2*math.pi):
                giro_anterior = 0
            giro_anterior = giro + giro_anterior
            rastro.append((pos_anterior_x, pos_anterior_y))
        
            # time.sleep(1)      Esto lo colocamos mañana
            # bot.drive_stop()   Esto lo colocamos mañana
                # Dibujar mapa
            dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro) 
            print('X: ' + str(pos_anterior_x))
            print('Y: ' + str(pos_anterior_y))
            print('giro: ' + str(giro_anterior))

            datos= bot.get_sensors()
            Encoder_izq = datos.encoder_counts_left
            Encoder_der = datos.encoder_counts_right
            # Gira a la izquierda
            bot.drive_direct(100, -100)
            time.sleep(0.2)

            # Obtener los datos de los sensores
            datos= bot.get_sensors()
            Encoder_izq_Act = datos.encoder_counts_left
            Encoder_der_Act = datos.encoder_counts_right

            Encoder_der_Act = Encoder_der_Act - Encoder_der
            Encoder_izq_Act = Encoder_izq_Act - Encoder_izq
            historico_der.append(-100)  
            historico_izq.append(100)  

            Desplazamiento_der = Encoder_der_Act * conversion
            Desplazamiento_izq = Encoder_izq_Act * conversion

            avance_promedio = (Desplazamiento_der + Desplazamiento_izq) / 2


            giro = ((Desplazamiento_der - Desplazamiento_izq)/ EJE_RUEDAS)

            inc_x = avance_promedio * math.cos(giro_anterior+giro)
            inc_y = avance_promedio * math.sin(giro_anterior+giro)
            pos_anterior_x = inc_x + pos_anterior_x
            pos_anterior_y = inc_y + pos_anterior_y

            if giro_anterior > 2*math.pi:
                giro_anterior = 0
            if giro_anterior <= (-2*math.pi):
                giro_anterior = 0
            giro_anterior = giro + giro_anterior
            rastro.append((pos_anterior_x, pos_anterior_y))
        
            # time.sleep(1)      Esto lo colocamos mañana
            # bot.drive_stop()   Esto lo colocamos mañana
                # Dibujar mapa
            dibujar_mapa(pos_anterior_x, pos_anterior_y, rastro) 
            print('X: ' + str(pos_anterior_x))
            print('Y: ' + str(pos_anterior_y))
            print('giro: ' + str(giro_anterior))

            #Guardamos datos primera pared para finalizar ahi -> QUE EL ROBOT SEPA QUE YA DIO LA VUELTA (NO SÉ COMO AJJAJAJJA)
            if not primera_pared:
                #datos_inicio = los que sea   

                primera_pared = True
        
        elif (luz_der >= 3000 or luz_frontal_der>= 3000) and primera_pared: # Si se deja de detectar la pared a la derecha, seguir la pared, EL SENSOR DEVUELVE UN NUMERO MAYOR CUANTO MAS CERCA ESTA DE LA PARED
            # DUDA -> NO SE SI SE DEBERIA DE MOVER ALANTE AQUI
            """
            bot.drive_direct(100, 100)
            bot.wait_time(0.1)
            """

            #Girar a la derecha 
            bot.drive_direct(100,-100)
            time.sleep(0.2)
            


def mostrar_texto(texto, x, y, tamano=20):
    fuente = pygame.font.SysFont(None, tamano)
    superficie_texto = fuente.render(texto, True, BLANCO)
    rectangulo_texto = superficie_texto.get_rect()
    rectangulo_texto.topleft = (x, y)
    screen.blit(superficie_texto, rectangulo_texto)
# Crear una instancia de Create2 y establecer la conexión
port = "COM7"  # Puerto serial donde está conectado el Roomba
bot = Create2(port)
bot.start()
bot.safe()

# Bucle para detectar las teclas presionadas y controlar el Roomba
conversion = calularConversion()
print('Conversion: ' + str(conversion))
with kb.Listener(pulsa) as escuchador:
    escuchador.join()    # Esperar hasta que se presione la tecla 'Esc' para detener el programa

# Cerrar la conexión al finalizar
bot.drive_stop()
bot.close()
