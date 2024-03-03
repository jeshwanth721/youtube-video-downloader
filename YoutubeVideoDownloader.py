import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

class YoutubeDownloaderApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YouTube Video Downloader")

        # Create widgets
        self.url_label = tk.Label(self.root, text="Enter YouTube URL:")
        self.url_entry = tk.Entry(self.root, width=40)
        self.download_button = tk.Button(self.root, text="Download", command=self.download_video)

        # Pack widgets
        self.url_label.pack(pady=10)
        self.url_entry.pack(pady=5)
        self.download_button.pack(pady=10)

    def open_file_dialog(self):
        folder = filedialog.askdirectory()
        if folder:
            return folder
        return None

    def download_video(self):
        video_url = self.url_entry.get()
        save_dir = self.open_file_dialog()

        if save_dir:
            try:
                yt = YouTube(video_url)
                streams = yt.streams.filter(progressive=True, file_extension="mp4")
                highest_res_stream = streams.get_highest_resolution()
                highest_res_stream.download(output_path=save_dir)
                print("Video downloaded successfully!")
                self.show_success_message()
            except Exception as e:
                print(f"Error downloading video: {e}")
        else:
            print("Invalid save location.")

    def show_success_message(self):
        success_window = tk.Toplevel(self.root)
        success_window.title("Success")
        success_window.geometry("300x100")
        success_label = tk.Label(success_window, text="Video Downloaded Successfully!")
        success_label.pack(pady=20)
        success_window.after(5000, success_window.destroy)  # Close after 5 seconds

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = YoutubeDownloaderApp()
    app.run()
