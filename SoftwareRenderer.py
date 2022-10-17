from gl import *


# Valores aleatorios
import random


# Colores
red = color(1, 0, 0)
wh = color(1, 1, 1)

# Definicion de variables para versión aleatoria
firstValue = random.random()
secondValue = random.random()
thirdValue = random.random()

firstColor = random.randint(0, 1)
secondColor = random.randint(0, 1)
thirdColor = random.randint(0, 1)

firstX = random.randint(0, 1)
firstY = random.randint(0, 1)


def SoftwareRender1(fileName):
    r = Render(1000, 1000)
    r.glClearColor(firstValue, secondValue, thirdValue)
    r.glClear()
    r.glClearViewPort(color(0, 0, 0))
    r.glVertex(firstX, firstY, color(firstColor, secondColor, thirdColor))
    r.glFinish(fileName)


def SoftwareRender2(filename):

    r = Render(1000, 1000)

    # Parte lateral 1
    r.glLine(100, 300, 300, 100, red)
    r.glLine(100, 300, 100, 500, red)
    r.glLine(100, 300, 400, 300, red)

    # Pared izquierda
    r.glLine(300, 100, 500, 100, red)
    r.glLine(400, 300, 500, 100, red)

    # Puerta
    r.glLine(100, 500, 250, 500, red)
    r.glLine(100, 650, 250, 650, red)
    r.glLine(250, 650, 250, 500, red)

    # Parte lateral 2
    r.glLine(100, 650, 100, 850, red)

    # Pared derecha
    r.glLine(100, 850, 400, 850, red)

    # Techo
    r.glLine(400, 850, 600, 600, red)
    r.glLine(600, 600, 400, 300, red)

    # Techo en 3D
    r.glLine(500, 100, 700, 400, red)
    r.glLine(600, 600, 700, 400, red)

    r.glFinish(filename)
