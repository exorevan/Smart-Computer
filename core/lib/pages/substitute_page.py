from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

from core.lib.handlers.crypt.substitute.simple_substitute import SimpleSubstitute


class SubstitutePage(QDialog):
    def __init__(self, widget) -> None:
        super(SubstitutePage, self).__init__()
        loadUi("core/lib/uis/substitution/Substitution.ui", self)
        self.backButton.clicked.connect(self._go_back)

        self.encodeButton.clicked.connect(self._encode)
        self.decodeButton.clicked.connect(self._decode)

        self.widget = widget

    def _go_back(self) -> None:
        self.widget.setCurrentIndex(0)

    def _encode(self) -> None:
        simp_sub = SimpleSubstitute()
        simp_sub.sub_type = self.typeEdit.toPlainText()
        simp_sub.cesar_offset = self.offsetEdit.toPlainText()
        self.resultEdit.setText(simp_sub.encrypt(self.textEdit.toPlainText()))

    def _decode(self) -> None:
        simp_sub = SimpleSubstitute()
        simp_sub.sub_type = self.typeEdit.toPlainText()
        simp_sub.cesar_offset = self.offsetEdit.toPlainText()
        self.resultEdit.setText(simp_sub.decrypt(self.textEdit.toPlainText()))
    