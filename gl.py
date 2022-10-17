# Modulo para estructura de bytes

import struct


# Valores constantes a usar
color1 = "white"
color2 = "black"
minMax = 0.9999
halfScreenSize = 500

from collections import *


def char(c):
    return struct.pack("=c", c.encode("ascii"))


def word(w):
    return struct.pack("=h", w)


def dword(d):
    return struct.pack("=l", d)


def VerifyIntegers(value):
    try:
        value = int(value)

    except:
        print("Error")


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


def BasicColors(const):
    if const == "white":
        return color(1, 1, 1)
    if const == "black":
        return color(0, 0, 0)


def VertexOperation(position, viewDimension, viewPosition):
    pos = (position + 1) * (viewDimension / 2) + viewPosition
    pos = int(pos)
    return pos


class Render(object):
    # (05 puntos) Deben crear una función glInit() que inicialice cualquier objeto interno que requiera su software renderer
    def __init__(self, width, height):
        self.glInit(width, height)

    def glInit(self, width, height) -> None:
        self.glCreateWindow(width, height)
        self.clearColor = BasicColors("black")
        self.currentColor = BasicColors("white")
        self.glClear()

    # (05 puntos) Deben crear una función glCreateWindow(width, height) que inicialice su framebuffer con
    # un tamaño (la imagen resultante va a ser de este tamaño).
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height
        self.glViewPort(0, 0, self.width, self.height)

    # (10 puntos)  Deben crear una función glViewPort(x, y, width, height) que defina el área de la imagen sobre la que se va a poder dibujar
    def glViewPort(self, x, y, width, height):
        self.viewPortX = x
        self.viewPortY = y
        self.viewPortWidth = width
        self.viewPortHeight = height

    # (10 puntos) Deben crear una función glClearColor(r, g, b) con la que se pueda cambiar el color con el que funciona glClear().
    # Los parámetros deben ser números en el rango de 0 a 1.
    def glClearColor(self, r, g, b):
        self.clearColor = color(r, b, g)

    def glClearViewPort(self, color=None):
        for x in range(self.viewPortX, self.viewPortX + self.viewPortWidth):
            for y in range(self.viewPortY, self.viewPortY + self.viewPortHeight):
                self.glPoint(x, y, color)

    def glPoint(self, x, y, color=None) -> None:
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y] = color or self.currentColor

    def glPointViewport(self, x, y, color=None):
        if x < -1 or x > 1 or y < -1 or y > 1:
            return
        tempX = x + 1
        tempY = y + 1
        tempVw = self.viewPortWidth / 2
        tempVh = self.viewPortHeight / 2
        finalX = tempX * tempVw + self.viewPortX
        finalY = tempY * tempVh + self.viewPortY
        try:
            finalX = int(finalX)
            finalY = int(finalY)
        except ValueError:
            print("Error ")

        self.glPoint(finalX, finalY, color)

    def glLine(self, x0, y0, x1, y1, color=None) -> None:

        tempX0 = int(x0)
        tempX1 = int(x1)
        tempY0 = int(y0)
        tempY1 = int(y1)

        if tempX0 == tempX1:
            if tempY0 == tempY1:
                self.glPoint(tempX0, tempY0, color)

        dx = abs(tempX1 - tempX0)
        dy = abs(tempY1 - tempY0)

        steep = dy > dx

        if steep:
            tempX0, tempY0 = tempY0, tempX0
            tempX1, tempY1 = tempY1, tempX1

        if tempX1 < tempX0:
            tempX0, tempX1 = tempX1, tempX0
            tempY0, tempY1 = tempY1, tempY0

        dx = abs(tempX1 - tempX0)

        dy = abs(tempY1 - tempY0)

        offset = 0
        limite = 0.5
        ecuacionRecta = dy / dx

        finalY = tempY0

        for i in range(tempX0, tempX1 + 1):
            self.glPoint(finalY, i, color) if steep else self.glPoint(i, finalY, color)
            offset += ecuacionRecta
            if limite <= offset:
                finalY = finalY + 1 if tempY0 < tempY1 else finalY - 1
                limite += 1

    # (20 puntos) Deben crear una función glClear() que llene el mapa de bits con un solo color
    def glClear(self):
        self.pixels = [
            [self.clearColor for y in range(self.height)] for x in range(self.width)
        ]
        self.zbuffer = [
            [float("inf") for y in range(self.height)] for x in range(self.width)
        ]

    def viewPortDivision(value, division):
        view = value / division
        view = int(view)
        return view

    # (30 puntos) Deben crear una función glVertex(x, y, color) que pueda cambiar el color de un punto de la pantalla.
    def glVertex(self, x, y, color=None):
        if x > minMax or x < -minMax:
            x, y = halfScreenSize
            self.pixels[x][y] = color or self.current_color
        if y > minMax or y < -minMax:
            x, y = halfScreenSize
            self.pixels[x][y] = color or self.current_color
        else:
            posX = VertexOperation(x, self.viewPortWidth, self.viewPortX)
            posY = VertexOperation(y, self.viewPortHeight, self.viewPortY)
            try:
                if 0 <= x < self.width:
                    if 0 <= y < self.height:
                        self.pixels[posX][posY] = color or self.current_color
            except:
                print("OOP! Ha ocurrido un error... :c")

    # (15 puntos) Deben crear una función glColor(r, g, b) con la que se pueda cambiar el color con el que funciona glVertex().
    # Los parámetros deben ser números en el rango de 0 a 1
    def glColor(self, r, g, b):
        self.current_color = color(r, g, b)

    def glFinish(self, filename):
        with open(filename, "wb") as f:
            f.write(char("B"))
            f.write(char("M"))
            f.write(dword(54 + self.width * self.height * 3))
            f.write(dword(0))
            f.write(dword(54))
            f.write(dword(40))
            f.write(dword(self.width))
            f.write(dword(self.height))
            f.write(word(1))
            f.write(word(24))
            f.write(dword(0))
            f.write(dword(self.width * self.height * 3))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))
            f.write(dword(0))

            for x in range(self.height):
                for y in range(self.width):
                    f.write(self.pixels[x][y])
            f.close()
