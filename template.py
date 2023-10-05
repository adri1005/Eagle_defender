import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Definir dimensiones de la ventana
ANCHO = 500
ALTO = 400
fuente_botones = pygame.font.SysFont(None, 30)

# Crear la ventana principal
ventana_principal = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Navegación entre ventanas')

# Crear la ventana de inicio
def ventana_inicio():
    # Crear la ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Ventana de inicio')

    # Crear los botones
    boton_registro = pygame.Rect(200, 150, 200, 80)
    boton_inicio_sesion = pygame.Rect(200, 250, 200, 80)

    # Crear la fuente para el texto de los botones
    fuente_botones = pygame.font.SysFont(None, 30)

    # Renderizar el texto de los botones en una superficie de Pygame
    texto_registro = fuente_botones.render('Registrarse', True, BLANCO)
    texto_inicio_sesion = fuente_botones.render('Iniciar sesión', True, BLANCO)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_registro.collidepoint(evento.pos):
                    ventana_registro()
                if boton_inicio_sesion.collidepoint(evento.pos):
                    ventana_inicio_sesion()

        # Dibujar los botones en la pantalla
        pygame.draw.rect(ventana, (255, 0, 0), boton_registro)
        pygame.draw.rect(ventana, (0, 255, 0), boton_inicio_sesion)

        # Dibujar el texto de los botones en la pantalla
        ventana.blit(texto_registro, (boton_registro.x + 20, boton_registro.y + 20))
        ventana.blit(texto_inicio_sesion, (boton_inicio_sesion.x + 20, boton_inicio_sesion.y + 20))

        # Actualizar la pantalla
        pygame.display.update()

# Crear la ventana de registro
def ventana_registro():
    # Crear la ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Ventana de registro')

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Actualizar la pantalla
        pygame.display.update()

# Crear la ventana de inicio de sesión
def ventana_inicio_sesion():
    # Crear la ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Ventana de inicio de sesión')

    # Crear la fuente para el texto de los botones
    fuente_botones = pygame.font.SysFont(None, 30)

    # Crear el botón para volver a la ventana principal
    boton_volver = pygame.Rect(50, 50, 200, 80)
    texto_volver = fuente_botones.render('Volver', True, BLANCO)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    ventana_inicio()

        # Dibujar el botón en la pantalla
        pygame.draw.rect(ventana, (0, 0, 255), boton_volver)
        ventana.blit(texto_volver, (boton_volver.x + 20, boton_volver.y + 20))

        # Actualizar la pantalla
        pygame.display.update()

# Iniciar la aplicación con la ventana de inicio
ventana_inicio()
