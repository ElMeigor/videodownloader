import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import time

#tkinter named as tk
#root is the name of the window
root = tk.Tk()

#Easy calling to handle post-download operation
def Main_Function_Caller():
    video_downloader()
    progress()

#Progress Bar
def progress():
    y = 0
    for x in range(4):
        my_progress['value'] += 25
        root.update_idletasks()
        time.sleep(1)
    completed_text()

#Downloads Video From Given URL
def video_downloader():
    thevideo = videourl.get()
    youtubeObject = YouTube(thevideo)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    use_oauth=False
    allow_oauth_cache=True
    try:
        youtubeObject.download('videos')
    except:
        print("Didn't work :(")

#Download Completed Text
def completed_text():
    download_complete.configure(text="Download Complete!")

#Download Complete Text
download_complete = tk.Label(root, text="")
download_complete.pack(padx=20, pady=20)

#Root Progress Bar
my_progress = ttk.Progressbar(root, length=300)
my_progress.pack(pady=20)

#Set window dimensions of x by y and title it
root.geometry("500x300")
root.title("Meister Video Downloader")

#Root Label Text
label = tk.Label(root, text="Paste the link and click download :)", font=('Arial', 18))
label.pack(padx=20, pady=10)

#Root User Input
videourl = tk.Entry(root, width=200)
videourl.pack(padx=30)

#Root Download Button
download = tk.Button(root, text="Download", command=Main_Function_Caller)
download.pack(padx=20)

root.mainloop()
