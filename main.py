import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from core.lib.handlers.crypt.substitute.simple_substitute import SimpleSubstitute
from core.lib.handlers.crypt.transposition.simple_transposition import SimpleTransposition

from core.lib.pages.start_page import StartPage
from core.lib.pages.substitute_page import SubstitutePage
from core.lib.pages.transposition_page import TransposePage
    

if __name__ == "__main__":
    """
        Indicies:
            0 - Start
            1 - Substitute
            2 - Transpose
    """

    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    start = StartPage(widget)
    substitute = SubstitutePage(widget)
    transpose = TransposePage(widget)

    widget.addWidget(start)
    widget.addWidget(substitute)
    widget.addWidget(transpose)
    widget.show()

    sys.exit(app.exec())