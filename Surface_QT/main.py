import sys
from PyQt4 import QtGui

from MainWindow import Ui_MainWindow
from GLWidget import GLWidget


class App(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Add OpenGL widget to main window
        self.gl_widget = GLWidget(self)
        self.ui.main_layout.addWidget(self.gl_widget)

        #Connect gui controls to model
        self.ui.zoom_slider.valueChanged.connect(self.gl_widget.zoom)
        self.ui.elevation_slider.valueChanged.connect(self.gl_widget.elevation)
        self.ui.azimuth_slider.valueChanged.connect(self.gl_widget.azimuth)
        self.ui.wireframe_check.toggled.connect(self.gl_widget.wire)
        self.ui.axes_check.toggled.connect(self.gl_widget.show_axes)
        self.ui.perspective_check.toggled.connect(self.gl_widget.set_projection)

app = QtGui.QApplication(sys.argv)
gui = App()
gui.show()
sys.exit(app.exec_())
