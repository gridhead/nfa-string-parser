from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import NonDeterministicFA
import sys, time

PrimaryUserInterface,_ = loadUiType("BaseUserInterface.ui")
SecondaryUserInterface,_ = loadUiType("HelpUserInterface.ui")

class HelpApp(QMainWindow,SecondaryUserInterface):
    def __init__(self, parent=None):
        super(HelpApp, self).__init__(parent)
        self.title = "NFA-String Parser - Help Page"
        self.setupUi(self)
        self.setWindowTitle(self.title)

class MainApp(QMainWindow,PrimaryUserInterface):
    def __init__(self):
        QMainWindow.__init__(self)
        self.title = "NFA-String Parser by t0xic0der"
        self.setupUi(self)
        self.setWindowTitle(self.title)
        self.HandleElements()
        self.HelpDialogBox = HelpApp()

    def HandleElements(self):
        self.otptbody.setReadOnly(True)
        self.parsebtn.clicked.connect(self.ParseString)
        self.helpebtn.clicked.connect(self.ShowHelpPage)

    def ShowHelpPage(self):
        self.HelpDialogBox.show()

    def ParseString(self):
        InputNFAText = self.nfatinpt.toPlainText()
        InputTestString = self.testinpt.text()
        DisplayVariable = "<b>Started FA-String parsing engine</b>" + "<br/><i>" + time.ctime() + "</i><br/>"
        try:
            DisplayVariable = DisplayVariable + NonDeterministicFA.MainFunction(InputNFAText, InputTestString)
        except BaseException as ExceptionEvent:
            DisplayVariable = DisplayVariable + "<br/><b>Failure: </b>" + str(ExceptionEvent) + "<br/>"
        DisplayVariable = DisplayVariable + "<br/>" + "<b>Stopped FA-String parsing engine</b>" + "<br/>" + \
                          "<i>Follow me on https://www.github.com/t0xic0der for more such projects!</i>"
        self.otptbody.setText(DisplayVariable)

def main():
    app=QApplication(sys.argv)
    QFontDatabase.addApplicationFont("Roboto-Regular.ttf")
    QFontDatabase.addApplicationFont("RobotoMono-Regular.ttf")
    QFontDatabase.addApplicationFont("RobotoMono-Italic.ttf")
    QFontDatabase.addApplicationFont("RobotoMono-Bold.ttf")
    window=MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()