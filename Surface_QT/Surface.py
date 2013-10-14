# -*- coding: utf-8 -*-
from OpenGL.GL import *
from utils import *

from scipy.spatial import Delaunay
import numpy as np


class Surface:

    def __init__(self, filename=''):

        self.filename = filename
        self.lista = 0
        
        self.crear()

    def crear(self):
        triangulos = []
        points = np.loadtxt(self.filename, delimiter=',')
        points[:, 2] = points[:, 2]-np.amin(points[:, 2])
        points[:, 0] = points[:, 0]-np.mean(points[:, 0])
        points[:, 1] = points[:, 1]-np.mean(points[:, 1])
        points2d = points[:, (0, 1)]
        tri = Delaunay(points2d)
        
        for v in tri.vertices:
            for i in v:
                t = Vector(points[i, 0], points[i, 1], points[i, 2])
                triangulos.append(t)
        
        self.lista = glGenLists(1)
        glNewList(self.lista, GL_COMPILE)

        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        
        glMaterial(GL_FRONT_AND_BACK, GL_AMBIENT, [0.0, 0.0, 0.0])
        glMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.4, 0.4, 0.4])
        glMaterial(GL_FRONT_AND_BACK, GL_SPECULAR, [0.0, 0.0, 0.0])
        glMaterialfv(GL_FRONT, GL_EMISSION, [0, 0, 0, 1.0])
        glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 1)
        
        glColor4fv([130/255.0, 95/255.0, 50/255.0, 1.0])
        
        glBegin(GL_TRIANGLES)
        i = 0
        while i < len(triangulos):
            n = normal(triangulos[i], triangulos[i+1], triangulos[i+2])
            if n.z > 0:
                triangulo(triangulos[i], triangulos[i+1], triangulos[i+2])
            else:
                triangulo(triangulos[i], triangulos[i+2], triangulos[i+1])
            i += 3
        glEnd()

        glEndList()

    def dibujar(self):
        glCallList(self.lista)
