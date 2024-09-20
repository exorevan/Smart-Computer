import sys
from typing import NoReturn

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QStackedWidget

from core.lib.handlers.handler_interface import Handler
from core.lib.pages.base.start_page import StartPage
from core.lib.pages.crypt.custom_block_page import CustomBlockPage
from core.lib.pages.crypt.double_file_page import DoubleFilePage
from core.lib.pages.crypt.single_file_page import SingleFilePage
from core.lib.pages.crypt.substitute_page import SubstitutePage
from core.lib.pages.crypt.transposition_page import TransposePage
from core.lib.pages.videodownloaders.vk_video_downloader_page import \
    VKVideoDownloaderPage


class MainApplication(Handler):
    def __init__(self) -> None:
        self.handler_name = "Main Application"

    @classmethod
    def run(cls) -> NoReturn:
        app: QApplication = QApplication(sys.argv)
        widget: QStackedWidget = QtWidgets.QStackedWidget()

        start: StartPage = StartPage(widget)
        substitute: SubstitutePage = SubstitutePage(widget)
        transpose: TransposePage = TransposePage(widget)
        singleFile: SingleFilePage = SingleFilePage(widget)
        doubleFile: DoubleFilePage = DoubleFilePage(widget)
        cipherBlock: CustomBlockPage = CustomBlockPage(widget)
        vkvideodownloaderBlock: VKVideoDownloaderPage = VKVideoDownloaderPage(widget)

        _ = widget.addWidget(start)
        _ = widget.addWidget(substitute)
        _ = widget.addWidget(transpose)
        _ = widget.addWidget(singleFile)
        _ = widget.addWidget(doubleFile)
        _ = widget.addWidget(cipherBlock)
        _ = widget.addWidget(vkvideodownloaderBlock)
        _ = widget.show()

        sys.exit(app.exec())


if __name__ == "__main__":
    """
    Indicies:
        0 - Start
        1 - Substitute
        2 - Transpose
        3 - Sinfle-file
        4 - Double-file
        5 - Double-file
    """

    MainApplication.run()
