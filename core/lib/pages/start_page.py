from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi


class StartPage(QDialog):
    def __init__(self, widget) -> None:
        super(StartPage, self).__init__()
        loadUi("core/lib/uis/start/Start.ui", self)
        self.openSubstituteButton.clicked.connect(self._openSubstitutePage)
        self.openTranspositionButton.clicked.connect(self._openTranspositionPage)
        self.openSingleFileButton.clicked.connect(self._openSingleFilePage)
        self.openDoubleFileButton.clicked.connect(self._openDoubleFilePage)
        self.openBlockCipherButton.clicked.connect(self._openBlockCipherPage)

        self.widget = widget

    def _openSubstitutePage(self) -> None:
        self.widget.setCurrentIndex(1)

    def _openTranspositionPage(self) -> None:
        self.widget.setCurrentIndex(2)
    
    def _openSingleFilePage(self) -> None:
        self.widget.setCurrentIndex(3)

    def _openDoubleFilePage(self) -> None:
        self.widget.setCurrentIndex(3)

    def _openBlockCipherPage(self) -> None:
        self.widget.setCurrentIndex(3)
