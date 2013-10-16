# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *


#----------------------------- CLASE VECTOR ----------------------------------#
class Vector:
    """
    Define un objeto vector en 3D. Contiene los parametros [X,Y,Z] que
    permiten ubicarse en el espacio 3D. Provee metodos para transformar entre
    sistemas de coordenadas esfericas, cilindricas y cartesianas.

    @ Param: x, y, z - componentes del vector, enteros o reales.
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def fi(self):
        return atan2(self.y, self.x)

    def theta(self):
        return acos(self.z/self.modulo())

    def rho(self):
        return (self.x**2 + self.y**2)**0.5

    def modulo(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def esfericas(self):
        return self.modulo(), self.fi(), self.theta()

    def cilindricas(self):
        return self.rho(), self.fi(), self.z

    def cartesianas(self):
        return self.x, self.y, self.z
#------------------------------------------------------------------------------#


#------------------- FUNCIONES PARA MANIPULAR VECTORES ------------------------#
def VectorEsfericas(r, fi, theta):
    """
    @ VectorEsfericas: Crea un nuevo objeto Vector dando sus coordenadas en esfericas
    @ Param: r, fi, theta - coordenadas en esfericas, enteros o reales.
    """
    return Vector(r*sin(theta)*cos(fi), r*sin(theta)*sin(fi), r*cos(theta))


def VectorCilindricas(r, fi, z):
    """
    @ VectorCilindricas: Crea un nuevo objeto Vector dando sus coordenadas cilindr.
    @ Param: r, fi, z - coordenadas en cilindricas, enteros o reales.
    """
    return Vector(r*cos(fi), r*sin(fi), z)


def sumar(r2, r1):
    return Vector(r2.x + r1.x, r2.y + r1.y, r2.z + r1.z)


def restar(r2, r1):
    return Vector(r2.x - r1.x, r2.y - r1.y, r2.z - r1.z)


def multiplicar(r2, r1):
    return Vector(r2.x * r1.x, r2.y * r1.y, r2.z * r1.z)


def ponderar(a, r):
    return Vector(a*r.x, a*r.y, a*r.z)


def normalizar(r):
    m=r.modulo()
    if m>0:
        return Vector(r.x/m, r.y/m)
    else:
        return r


def desplazarRadialmente(r, d):
    return VectorEsfericas(r.modulo()+d, r.fi(), r.theta())


def rotarFi(r, a):
    a2 = r.fi()+a
    if a2 >= 2*pi:
        a2 -= 2*pi
    if a2 < 0:
        a2 += 2*pi
    return VectorCilindricas(r.rho(), a2, r.z)


def rotarTheta(r,a):
    a2=r.theta()+a
    if a2>=pi:
        a2=a2-2*pi
    if a2<-pi:
        a2=a2+2*pi
    return VectorEsfericas(r.modulo(),r.fi(),a2)


def distancia(r1, r2):
    return restar(r1, r2).modulo()


def punto(r1,r2):
    return r1.x*r2.x + r1.y*r2.y + r1.z*r2.z


def cruz(r1,r2):
    return Vector(r1.y*r2.z - r1.z*r2.y, r1.z*r2.x - r1.x*r2.z, r1.x*r2.y - r1.y*r2.x)


def normal(r0, r1, r2):
    """
    Retorna un objeto Vector que es la normal de un triangulo definido por
    tres vectores segun la regla de la mano derecha.
    @ Param: r0, r1, r2 - Objetos de la clase Vector
    """
    n = cruz(restar(r1, r0), restar(r2, r0))
    m = n.modulo()
    if m != 0:
        return ponderar(1.0/m, n)
    else:
        return n


def promediar(lv):
    n = len(lv)

    r = Vector(0.0, 0.0, 0.0)

    for v in lv:
        r = sumar(r, ponderar(1.0/n, v))

    return r
#------------------------------------------------------------------------------#


#------------------ FUNCIONES PARA DIBUJAR PRIMITIVAS -------------------------#
def triangulo(p1, p2, p3):
    """
    Genera los vertices para un triangulo en 3D. Util para dibujar
    figura complejas en 3D utilizando siempre caras planas.
    @ Param: p1, p2, p3 - Objetos de la clase Vector
    """
    glNormal3fv(normal(p1, p2, p3).cartesianas())
    glVertex3fv(p1.cartesianas())
    glVertex3fv(p2.cartesianas())
    glVertex3fv(p3.cartesianas())


def cuadrilatero(p1, p2, p3, p4):
    """
    Genera los vertices para un cuadrilatero en 3D en base a
    triangulos.
    @ Param: p1, p2, p3, p4: Objetos de la clase Vector
    """
    triangulo(p1, p4, p3)
    triangulo(p3, p2, p1)

#------------------------------------------------------------------------------#

#--------------------------- CLASE CAMARA -------------------------------------#

#  (UP)
#   ^
#   |
#  (EYE)----------------------> [AT]

class Camara:
    def __init__(self, eye, at, up):
        self.eye = eye
        self.at = at
        self.up = up

    def lookAt(self):
        glLoadIdentity()
        gluLookAt(self.eye.x, self.eye.y, self.eye.z,
                  self.at.x, self.at.y, self.at.z,
                  self.up.x, self.up.y, self.up.z)
class Eje:
    def __init__(self, largo):
        self.largo = largo
        self.show = True

    def crear(self):
        pass

    def dibujar(self):
        if self.show:
            # almaceno la matriz, para aplicar los cambios solo sobre el Eje
            glDisable(GL_LIGHTING)

            glPushMatrix()
            glBegin(GL_LINES)

            # eje Y verde
            glColor4f(0.0, 1.0, 0.0, 1.0)
            glVertex4f(0.0, self.largo, 0.0, 1.0)
            glVertex4f(0.0,   0.0, 0.0, 1.0)
            # eje x rojo
            glColor4f(1.0, 0.0, 0.0, 1.0)
            glVertex4f(0.0, 0.0, 0.0, 1.0)
            glVertex4f(self.largo, 0.0, 0.0, 1.0)
            #eje z azul
            glColor4f(0.0, 0.0, 1.0, 1.0)
            glVertex4f(0.0, 0.0, 0.0, 1.0)
            glVertex4f(0.0, 0.0, self.largo, 1.0)
            glEnd()
            #importante, recupero la matriz!
            glPopMatrix()

            glEnable(GL_LIGHTING)