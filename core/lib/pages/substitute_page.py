from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi

from core.lib.handlers.crypt.substitute.simple_substitute import SimpleSubstitute


class SubstitutePage(QDialog):
    def __init__(self, widget) -> None:
        super(SubstitutePage, self).__init__()
        loadUi("core/lib/uis/substitution/Substitution.ui", self)
        self.backButton.clicked.connect(self.go_back)

        self.encodeButton.clicked.connect(self.encode)
        self.decodeButton.clicked.connect(self.decode)

        self.widget = widget

    def go_back(self) -> None:
        self.widget.setCurrentIndex(0)

    def encode(self) -> None:
        simp_sub = SimpleSubstitute()
        simp_sub.sub_type = self.typeEdit.toPlainText()
        simp_sub.cesar_offset = self.offsetEdit.toPlainText()
        self.resultEdit.setText(simp_sub.encrypt(self.textEdit.toPlainText()))

    def decode(self) -> None:
        simp_sub = SimpleSubstitute()
        simp_sub.sub_type = self.typeEdit.toPlainText()
        simp_sub.cesar_offset = self.offsetEdit.toPlainText()
        self.resultEdit.setText(simp_sub.decrypt(self.textEdit.toPlainText()))
    