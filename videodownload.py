import tkinter as tk
from tkinter import ttk
from pytube import YouTube

#tkinter named as tk
#root is the name of the window
root = tk.Tk()

#Video downloader based off var videourl
def videodownloader():
    thevideo = videourl.get()
    youtubeObject = YouTube(thevideo)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    use_oauth=False
    allow_oauth_cache=True
    try:
        youtubeObject.download('videos')
    except:
        print("Didn't work :(")
    print("Download completed!")

#Set window dimensions of x by y and title it
root.geometry("500x300")
root.title("Meister Video Downloader")

#Title basically
label = tk.Label(root, text="Paste the link and click download :)", font=('Arial', 18))
label.pack(padx=20, pady=10)

#Textbox value
videourl = tk.Entry(root)
videourl.pack(padx=30)

download = tk.Button(root, text="Download", command=videodownloader)
download.pack(padx=20)

root.mainloop()
