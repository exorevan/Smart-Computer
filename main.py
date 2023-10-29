import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from core.lib.handlers.handler_interface import Handler
from core.lib.handlers.crypt.substitute.simple_substitute import SimpleSubstitute
from core.lib.handlers.crypt.transposition.simple_transposition import SimpleTransposition

from core.lib.pages.start_page import StartPage
from core.lib.pages.substitute_page import SubstitutePage
from core.lib.pages.transposition_page import TransposePage
from core.lib.pages.single_file_page import SingleFilePage
    

class MainApplication(Handler):
    def __init__(self):
        self.handler_name = "Main Application"

    @classmethod
    def run(self):
        app = QApplication(sys.argv)
        widget = QtWidgets.QStackedWidget()

        start = StartPage(widget)
        substitute = SubstitutePage(widget)
        transpose = TransposePage(widget)
        singleFile = SingleFilePage(widget)

        widget.addWidget(start)
        widget.addWidget(substitute)
        widget.addWidget(transpose)
        widget.addWidget(singleFile)
        widget.show()

        sys.exit(app.exec())


if __name__ == "__main__":
    """
        Indicies:
            0 - Start
            1 - Substitute
            2 - Transpose
            3 - Sinfle-file
    """

    MainApplication.run()