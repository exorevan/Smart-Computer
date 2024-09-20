import typing as ty

import yt_dlp

from core.lib.handlers.videodownloders.videodownloader_handler_interface import \
    VideoDownloaderHandler


class VKVideoDownloader(VideoDownloaderHandler):
    def __init__(self) -> None:
        self.handler_name = "VK Downloader"

    def download_video(self, video_url: str) -> None:
        try:
            ydl_opts: dict[str, ty.Any] = {
                "outtmpl": "downloads/video/%(title)s.mp4",
                "quiet": True,
                "progress_hooks": [self.my_hook],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                _ = ydl.download(url_list=[video_url])
                _ = ydl.extract_info(url=video_url, download=True)
                pass
        except:
            pass

    def my_hook(self, d: dict[str, ty.Any]) -> None:
        if d["status"] == "downloading":
            percent_str = ty.cast(str, d["_percent_str"]).replace("[0;94m", "")
            percent_str: str = "".join(chr for chr in percent_str if chr.isprintable())
            percent: str = percent_str.split(sep="%")[0].strip()
            print(percent)
        elif d["status"] == "finished":
            pass

    def _run(self, video_url: str) -> None:
        self.download_video(video_url)
