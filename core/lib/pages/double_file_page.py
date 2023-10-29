from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

from core.lib.handlers.crypt.custom_file_crypt.double_file_crypt import DoubleFileCrypt


class DoubleFilePage(QDialog):
    def __init__(self, widget) -> None:
        super(DoubleFilePage, self).__init__()
        loadUi("core/lib/uis/custom/DoubleFileCrypt.ui", self)
        self.backButton.clicked.connect(self._go_back)

        self.encodeButton.clicked.connect(self._encode)
        self.decodeButton.clicked.connect(self._decode)

        self.widget = widget

    def _go_back(self) -> None:
        self.widget.setCurrentIndex(0)

    def _encode(self) -> None:
        simp_sub = DoubleFileCrypt()
        simp_sub.orig_file = self.origFileEdit.toPlainText()
        simp_sub.additional_file = self.additionalFileEdit.toPlainText()
        simp_sub.processed_file = self.processedFileEdit.toPlainText()
        self.resultEdit.setText(simp_sub.encrypt())

    def _decode(self) -> None:
        simp_sub = DoubleFileCrypt()
        simp_sub.orig_file = self.origFileEdit.toPlainText()
        simp_sub.additional_file = self.additionalFileEdit.toPlainText()
        simp_sub.processed_file = self.processedFileEdit.toPlainText()
        self.resultEdit.setText(simp_sub.decrypt())
    