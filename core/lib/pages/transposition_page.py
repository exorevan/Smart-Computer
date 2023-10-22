from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

from core.lib.handlers.crypt.transposition.simple_transposition import SimpleTransposition


class TransposePage(QDialog):
    def __init__(self, widget) -> None:
        super(TransposePage, self).__init__()
        loadUi("core/lib/uis/transposition/Transposition.ui", self)
        self.backButton.clicked.connect(self.go_back)

        self.encodeButton.clicked.connect(self.encode)
        self.decodeButton.clicked.connect(self.decode)

        self.widget = widget

    def go_back(self) -> None:
        self.widget.setCurrentIndex(0)

    def encode(self) -> None:
        simp_trans = SimpleTransposition()
        simp_trans.trans_type = self.typeEdit.toPlainText()
        simp_trans.cols_count = self.colsEdit.toPlainText()
        self.resultEdit.setText(simp_trans.encrypt(self.textEdit.toPlainText()))

    def decode(self) -> None:
        simp_trans = SimpleTransposition()
        simp_trans.trans_type = self.typeEdit.toPlainText()
        simp_trans.cols_count = self.colsEdit.toPlainText()
        self.resultEdit.setText(simp_trans.decrypt(self.textEdit.toPlainText()))
    