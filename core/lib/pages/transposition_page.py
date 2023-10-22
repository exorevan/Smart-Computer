from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

from core.lib.handlers.crypt.transposition.simple_transposition import SimpleTransposition


class TransposePage(QDialog):
    def __init__(self, widget) -> None:
        super(TransposePage, self).__init__()
        loadUi("core/lib/uis/transposition/Transposition.ui", self)
        self.backButton.clicked.connect(self._go_back)

        self.encodeButton.clicked.connect(self._encode)
        self.decodeButton.clicked.connect(self._decode)

        self.widget = widget

    def _go_back(self) -> None:
        self.widget.setCurrentIndex(0)

    def _encode(self) -> None:
        simp_trans = SimpleTransposition()
        simp_trans.trans_type = self.typeEdit.toPlainText()
        simp_trans.cols_count = self.colsEdit.toPlainText()
        self.resultEdit.setText(simp_trans.encrypt(self.textEdit.toPlainText()))

    def _decode(self) -> None:
        simp_trans = SimpleTransposition()
        simp_trans.trans_type = self.typeEdit.toPlainText()
        simp_trans.cols_count = self.colsEdit.toPlainText()
        self.resultEdit.setText(simp_trans.decrypt(self.textEdit.toPlainText()))
    