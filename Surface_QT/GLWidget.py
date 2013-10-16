from math import pi
# PyQT4 imports
#from PyQt4 import QtGui, QtCore, QtOpenGL
from PyQt4.QtOpenGL import QGLWidget

#PyOpenGL imports
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

#Own clases
from utils import *
from Surface import Surface


class GLWidget(QGLWidget):

    def __init__(self, parent):
        QGLWidget.__init__(self, parent)
        self.width = 640
        self.height = 480
        self.lenght = 640

        self.actors = []
        self.eye, self.at, self.up = 0, 0, 0
        self.camera = None
        self.axes = None

        # To update camera position from absolute values
        self.last_elev_factor = 0
        self.last_azim_factor = 0
        self.last_zoom_factor = 0

        self.l0_pos = []

    def initializeGL(self):
        """
        [Init]
        Initialize OpenGL, upload data on the GPU, etc.
        """
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glShadeModel(GL_SMOOTH)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

        self.l0_pos = [0.0, self.width, 10.0*self.height, 1.0]

        #glLightfv(GL_LIGHT0, GL_POSITION, self.l0_pos)
        glLightfv(GL_LIGHT0, GL_AMBIENT,  [0.4, 0.4, 0.4, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [0.99, 0.99, 0.99, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE,  [0.99, 0.99, 0.99, 1.0])

        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.4, 0.4, 0.4, 1])
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)

        self.eye = Vector(300, 0, 0)  # Posicion de la camara (Tripode)
        self.at = Vector(0.0, 0.0, 0.0)   # Hacia donde apunta (Objetivo)
        self.up = Vector(0.0, 0.0, 1.0)   # Giro de la camra (Enderezar)

        self.actors.append(Surface("surface_test.csv"))
        self.axes = Eje(200)
        self.camera = Camara(self.eye, self.at, self.up)

    def resizeGL(self, width, height):
        """
        [Reshape]
        Called upon window resizing: reinitialize the viewport
        """
        self.width = width
        self.height = height

        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(90, float(6*self.width)/float(6*self.height), 0.001*self.lenght, 6*self.lenght)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        """
        [Display]
        Drawing routine
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Actualizar pantalla
        glClearDepth(1.0)

        self.camera.lookAt()
        glLightfv(GL_LIGHT0, GL_POSITION, self.l0_pos)

        for actor in self.actors:
            actor.dibujar()

        self.axes.dibujar()

    def zoom(self, zoom_factor):
        """
        Updates zoom factor by moving eye vector radially
        Calculates eye displacement as a fraction of the distance between original
        eye and at vectors.
        """
        diff = (zoom_factor - self.last_zoom_factor)
        dist = distancia(self.eye, self.at)
        dist *= -diff/100.0
        self.camera.eye = desplazarRadialmente(self.camera.eye, dist)
        self.last_zoom_factor = zoom_factor
        self.updateGL()

    def elevation(self, elev_factor):
        """
        Updates elevation of the camera by moving eye vector in spherical coords.
        """
        diff = (elev_factor - self.last_elev_factor)/180.0*pi
        self.camera.eye = rotarTheta(self.camera.eye, -diff)
        self.last_elev_factor = elev_factor
        self.updateGL()

    def azimuth(self, azim_factor):
        """
        Updates azimuth positiion of the camera by moving eye vector in spherical coords.
        """
        diff = (azim_factor - self.last_azim_factor)/180.0*pi
        self.camera.eye = rotarFi(self.camera.eye, diff)
        self.last_azim_factor = azim_factor
        self.updateGL()

    def wire(self, on_wire):
        """
        Toggle display mode to wireframe or surface
        """
        if on_wire:
            glPolygonMode(GL_FRONT, GL_LINE)
            glPolygonMode(GL_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT, GL_FILL)
            glPolygonMode(GL_BACK, GL_FILL)

        self.updateGL()

    def show_axes(self, show):
        """
        Toggle axes display
        """
        self.axes.show = show
        self.updateGL()

    def set_projection(self, perspective_on):
        """
        Toggle projection mode to orthogonal or perspective
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        if perspective_on:
            gluPerspective(90, float(6*self.width)/float(6*self.height), 0.001*self.lenght, 6*self.lenght)
        else:
            glOrtho(-1*self.width, 1*self.width, -1*self.height, 1*self.height, -1*self.lenght, 1*self.lenght)

        glMatrixMode(GL_MODELVIEW)
        self.updateGL()
