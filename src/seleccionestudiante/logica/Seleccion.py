import sys
import os

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from tkinter import messagebox
from datetime import datetime
from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.Estudiante import Estudiante
from src.seleccionestudiante.modelo.Equipo import Equipo
from src.seleccionestudiante.modelo.Actividad import Actividad
from src.seleccionestudiante.logica.GestionAsignatura import GestionAsignatura
from src.seleccionestudiante.modelo.declarative_base import Session


class Dialogo(QDialog):
    # AusInUS = 2
    # UKInUS = 0.5
    # AusInUS = 3
    # UKInUS = 1.5

    def __init__(self):
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\WireFrameEditarAsignatura.ui"
        QDialog.__init__(self)
        uic.loadUi(ruta, self)


        self.btnGuardar.clicked.connect(self.EditarAsignatura)
        self.btnCancelar.clicked.connect(self.exit_app)

    def EditarAsignatura(self):
        resultado = messagebox.askquestion("¿Desea cambiar el nombre de la asignatura?")
        if resultado == "yes":
            IDAsignatura = self.lineEditAsignatura.text()
            NuevoNombreAsignatura = self.lineEditAsignaturaNuevo.text()
            resul = self.gestionAsignatura.editar_asignatura(asignatura_id = IDAsignatura, nombreAsignatura = NuevoNombreAsignatura)
            if resul == False:
                messagebox.showinfo('Mensaje Informativo', 'No se edito la asignatura')
            elif resul == True:
                messagebox.showinfo('Mensaje Informativo', 'Se edito la asignatura')
        if resultado == "no":
            messagebox.showinfo('Mensaje Informativo', 'No se edito la asignatura')


    def exit_app(self): #Si se presiona el boton cancelar la aplicacion mostrara un mensaje Salir
        resultado = messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            quit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    app.exec()