import tkinter
import customtkinter
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable, PytubeError

class YouTubeDownloader:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("720x480")
        self.app.title("YouTube Downloader")
        
        self.create_ui()
        self.app.mainloop()

    def create_ui(self):
        self.title_label = customtkinter.CTkLabel(self.app, text="Enter YouTube URL")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.url_var = tkinter.StringVar()
        self.url_entry = customtkinter.CTkEntry(self.app, textvariable=self.url_var, width=350)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.download_button = customtkinter.CTkButton(self.app, text="Download", command=self.download_video)
        self.download_button.grid(row=0, column=2, padx=10, pady=10)
        
        self.status_label = customtkinter.CTkLabel(self.app, text="")
        self.status_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def progress_function(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        per = f"{percentage_of_completion:.2f}%"
        self.status_label.configure(text=f"Downloading... {per}")
        self.app.update_idletasks()

    def download_video(self):
        url = self.url_entry.get()
        if not url:
            self.status_label.configure(text="Please enter a YouTube URL", text_color="red")
            return
        
        try:
            yt = YouTube(url, on_progress_callback=self.progress_function)
            video = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
            self.status_label.configure(text="Downloading...", text_color="blue")
            video.download()
            self.status_label.configure(text="Downloaded!", text_color="green")
        except RegexMatchError:
            self.status_label.configure(text="Invalid YouTube URL", text_color="red")
        except VideoUnavailable:
            self.status_label.configure(text="Video not available", text_color="red")
        except PytubeError:
            self.status_label.configure(text="Pytube error. Try updating Pytube.", text_color="red")
        except Exception as e:
            self.status_label.configure(text=f"Unexpected error: {e}", text_color="red")

if __name__ == "__main__":
    YouTubeDownloader()
