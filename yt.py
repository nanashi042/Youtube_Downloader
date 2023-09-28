import os
import yt_dlp

class vid_download:
    def __init__(self, url):
        self.url = url

    def download(self):
        output_path = "/temp/static/vid"
        file_name = "vid.mp4"

        # Delete the existing vid.mp4 file if it exists
        existing_file_path = os.path.join(output_path, file_name)
        if os.path.exists(existing_file_path):
            os.remove(existing_file_path)

        # Create youtube-dlp options
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{output_path}/{file_name}',
        }

        # Create a youtube-dlp YoutubeDL instance
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])

# Example usage:
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=eg65SbqmT0s"
    downloader = vid_download(video_url)
    downloader.download()
