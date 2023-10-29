from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

from core.lib.handlers.crypt.custom_file_crypt.block_cipher import CipherBlock


class CustomBlockPage(QDialog):
    def __init__(self, widget) -> None:
        super(CustomBlockPage, self).__init__()
        loadUi("core/lib/uis/custom/BlockCipherCrypt.ui", self)
        self.backButton.clicked.connect(self._go_back)

        self.encodeButton.clicked.connect(self._encode)
        self.decodeButton.clicked.connect(self._decode)

        self.widget = widget

    def _go_back(self) -> None:
        self.widget.setCurrentIndex(0)

    def _encode(self) -> None:
        simp_sub = CipherBlock()
        simp_sub.sub_type = 'custom'
        simp_sub.custom_offset = 10
        self.resultEdit.setText(simp_sub.encrypt(self.textEdit.toPlainText()))

    def _decode(self) -> None:
        simp_sub = CipherBlock()
        simp_sub.ty = 'custom'
        simp_sub.custom_offset = 10
        self.resultEdit.setText(simp_sub.decrypt(self.textEdit.toPlainText()))
    