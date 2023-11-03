import tkinter as tk
from tkinter import *
import pytube
from pytube import Playlist


# Define the function for the button

def audioBtn():
    try:
        url = input1.get()
        youtube = pytube.YouTube(url)
        audio = youtube.streams.filter(only_audio=True).first()
        fileName = input2.get()
        if fileName:
            fileName = fileName + '.mp3'
            audio.download(filename=fileName)
        else:
            youtube_title = youtube.title +'.mp3'
            audio.download(filename=youtube_title)
        result_label.config(text="File downloaded successfully",fg='green',font=(20))
    except:
        result_label.config(text="Url not found or Link error!",fg='red',font=(20))


def videoBtn():
    try:
        url = input1.get()
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        fileName = input2.get()
        if fileName:
            fileName = fileName + '.mp4'
            video.download(filename=fileName)
        else:
            video.download()
        result_label.config(text="File downloaded successfully",fg='green',font=(20))
    except:
        result_label.config(text="Url not found or Link error!",fg='red',font=(20))


def downloadPlaylist():
    try:
        pl = Playlist(input1.get())
        for video in pl.videos:
            stream = video.streams.get_highest_resolution()
            stream.download()
        result_label.config(text="File downloaded successfully",fg='green',font=(20))
    except:
        result_label.config(text="Url not found or Link error!",fg='red',font=(20))


# Create the GUI window
root = tk.Tk()
# Set the window title
root.title("YouTube Song Downloader")

# Set the window size
root.geometry("800x400+400+250")


#labels
label1 = tk.Label(root,text="URL : ")
label2 = tk.Label(root,text="FileName : ")
input1 = tk.Entry(root, width=40, font=(
    'Times New Roman', 16))
input2 = tk.Entry(root, width=40, font=(
    'Times New Roman', 16), justify="center")


button1 = tk.Button(root, text="Audio", cursor="hand2",font=('Helvetica',10), width=20, height=2,
                    borderwidth=4, fg="white", bg="#070A52", border=0, command=audioBtn)
button2 = tk.Button(root, text="Video",font=('Helvetica',10), cursor="hand2", width=20, height=2,
                    borderwidth=0, fg="white", bg="#D21312", border=0, command=videoBtn)
button3 = tk.Button(root, text="PlayList", cursor="hand2", width=20, height=2,
                    borderwidth=0, fg="white",font=('Helvetica',10), bg="#FFD93D", border=0,command=downloadPlaylist)

result_label = tk.Label(root, text="Results will appear here.")


fileName = input2.get()

# Add the widgets to the window
label1.grid(row=1,column=0,padx=20,pady=10)
label2.grid(row=2,column=0,padx=10,pady=10)

input1.grid(row=1, column=1,columnspan=2, padx=20, pady=40)
input2.grid(row=2, column=1,columnspan=2 ,padx=40, pady=0)

button1.grid(row=3, column=0, padx=50, pady=40)
button2.grid(row=3, column=1, padx=50, pady=10)
button3.grid(row=3, column=2,padx=50, pady=10)


result_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)


root.resizable(width=False,height=False)
root.mainloop()
