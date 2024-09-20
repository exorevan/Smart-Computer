from PyQt6.QtWidgets import QDialog, QStackedWidget
from PyQt6.uic import loadUi

from core.lib.handlers.videodownloders.vk_video_downloader import \
    VKVideoDownloader


class VKVideoDownloaderPage(QDialog):
    def __init__(self, widget: QStackedWidget) -> None:
        super(VKVideoDownloaderPage, self).__init__()
        loadUi("uis//videodownloaders/VKVideoDownloader.ui", self)
        self.backButton.clicked.connect(self._go_back)
        self.downloadButton.clicked.connect(self._download)

        self.widget = widget

    def _go_back(self) -> None:
        self.widget.setCurrentIndex(0)

    def _download(self) -> None:
        downloader_obj: VKVideoDownloader = VKVideoDownloader()
        downloader_obj._run(video_url=self.textEdit.toPlainText())
