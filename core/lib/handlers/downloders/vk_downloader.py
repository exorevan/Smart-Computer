from core.lib.handlers.downloders.downloader_handler_interface import DownloaderHandler


class VKDownloader(DownloaderHandler):
    def __init__(self) -> None:
        self.handler_name = "VK Downloader"
