import pygame
import random

pygame.init()

# Dimensiones de la ventana del juego
ventana_ancho = 640
ventana_alto = 480

# Tamaño de los bloques y la serpiente
bloque_tamano = 20

# Colores
color_blanco = (255, 255, 255)
color_amarillo = (255, 255, 0)
color_negro = (0, 0, 0)

# Crear la ventana del juego
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption('Juego de la Viborita')

# Función para mostrar el mensaje en pantalla
def mostrar_mensaje(mensaje):
    fuente = pygame.font.SysFont(None, 50)
    texto = fuente.render(mensaje, True, color_blanco)
    ventana.blit(texto, (ventana_ancho // 2 - texto.get_width() // 2, ventana_alto // 2 - texto.get_height() // 2))
    pygame.display.update()
    
# Función principal del juego
def juego_viborita():
    # Posición inicial de la cabeza de la serpiente
    cabeza_x = ventana_ancho // 2
    cabeza_y = ventana_alto // 2

    # Velocidad inicial de la serpiente
    velocidad_x = 0
    velocidad_y = 0

    # Lista para almacenar la posición del cuerpo de la serpiente
    cuerpo = []

    # Longitud inicial de la serpiente
    longitud = 1
    
    # Puntuación inicial
    puntaje = 0

    # Posición inicial de la comida
    comida_x = round(random.randrange(0, ventana_ancho - bloque_tamano) / bloque_tamano) * bloque_tamano
    comida_y = round(random.randrange(0, ventana_alto - bloque_tamano) / bloque_tamano) * bloque_tamano

    # Velocidad del juego (velocidad de la serpiente)
    reloj = pygame.time.Clock()
    fps = 20
    
    # Bucle principal del juego
    juego_terminado = False
    while not juego_terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and velocidad_x == 0:
                    velocidad_x = -bloque_tamano
                    velocidad_y = 0
                elif evento.key == pygame.K_RIGHT and velocidad_x == 0:
                    velocidad_x = bloque_tamano
                    velocidad_y = 0
                elif evento.key == pygame.K_UP and velocidad_y == 0:
                    velocidad_x = 0
                    velocidad_y = -bloque_tamano
                elif evento.key == pygame.K_DOWN and velocidad_y == 0:
                    velocidad_x = 0
                    velocidad_y = bloque_tamano

        cabeza_x += velocidad_x
        cabeza_y += velocidad_y

        # Detectar colisiones con los bordes de la ventana
        if cabeza_x < 0 or cabeza_x >= ventana_ancho or cabeza_y < 0 or cabeza_y >= ventana_alto:
            mostrar_mensaje('¡Perdiste! Presiona "R" para reiniciar')
            pygame.display.update()

            # Reiniciar el juego al presionar "R"
            esperando_reinicio = True
            while esperando_reinicio:
                for evento in pygame.event.get():
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            juego_viborita()
                            esperando_reinicio = False
                        elif evento.key == pygame.K_q:
                            juego_terminado = True
                            esperando_reinicio = False

            # Salir del bucle principal para volver a empezar el juego
            break

        # Actualizar el fondo de la ventana
        ventana.fill(color_negro)

        # Dibujar la comida
        pygame.draw.rect(ventana, color_amarillo, [comida_x, comida_y, bloque_tamano, bloque_tamano])

        # Agregar la posición actual de la cabeza a la lista del cuerpo
        cuerpo.append((cabeza_x, cabeza_y))

        # Mantener la longitud de la serpiente
        if len(cuerpo) > longitud:
            del cuerpo[0]

        # Detectar colisiones con el cuerpo de la serpiente
        for bloque in cuerpo[:-1]:
            if bloque == (cabeza_x, cabeza_y):
                mostrar_mensaje('¡Perdiste! Presiona "R" para reiniciar')
                pygame.display.update()

                # Reiniciar el juego al presionar "R"
                esperando_reinicio = True
                while esperando_reinicio:
                    for evento in pygame.event.get():
                        if evento.type == pygame.KEYDOWN:
                            if evento.key == pygame.K_r:
                                juego_viborita()
                                esperando_reinicio = False
                            elif evento.key == pygame.K_q:
                                juego_terminado = True
                                esperando_reinicio = False

                # Salir del bucle principal para volver a empezar el juego
                break

        # Dibujar el cuerpo de la serpiente
        for bloque in cuerpo:
            pygame.draw.rect(ventana, color_blanco, [bloque[0], bloque[1], bloque_tamano, bloque_tamano])

        pygame.display.update()

        # Detectar colisión con la comida
        if cabeza_x == comida_x and cabeza_y == comida_y:
            comida_x = round(random.randrange(0, ventana_ancho - bloque_tamano) / bloque_tamano) * bloque_tamano
            comida_y = round(random.randrange(0, ventana_alto - bloque_tamano) / bloque_tamano) * bloque_tamano
            longitud += 1
            puntaje += 10  # Aumentar la puntuación al comer la comida

        reloj.tick(fps)
        
        # Dibujar la puntuación en la ventana
        fuente = pygame.font.SysFont(None, 30)
        texto_puntaje = fuente.render(f'Score: {puntaje}', True, color_amarillo)
        ventana.blit(texto_puntaje, (10, 10))  # Muestra el puntaje en la esquina superior izquierda

        pygame.display.update()
        
    pygame.quit()
    
# Iniciar el juego
juego_viborita()
