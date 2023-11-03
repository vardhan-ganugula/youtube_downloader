import tkinter
import customtkinter
import pytube
from pytube import YouTube

# custom tkinter settings
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
app = customtkinter.CTk()
app.geometry("720x480+600+200")
app.title("YouTube Downloader")


#functions and stufff

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        finishLabel.configure(text="Download completed", text_color='green')
    except:
        finishLabel.configure(
            text="Download failed! Check link and Try again", text_color='red')



def on_progress(stream, chunk, bytes_reamining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_reamining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # update progress bar
    progressBar.set(float(percentage_of_completion) / 100)



def getDetails():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        title.configure(text=ytObject.title, text_color='white')

    except:
        title.configure(text='Details not found', text_color='red')


def audiosDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        audios = ytObject.streams.filter(only_audio=True).first()
        audios.download(filename=(ytObject.title+'.mp3'))
        finishLabel.configure(text="Download completed", text_color='green')
    except:
        finishLabel.configure(
            text="Download failed! Check link and Try again", text_color='red')



# title
title = customtkinter.CTkLabel(app, text="Youtube downloader",
                               font=("Robot", 20, 'bold'))
title.pack(padx=50, pady=20)

# input / entry box
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# progress precentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack(pady=20)

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# button
frameBtn = customtkinter.CTkFrame(master=app)
detailsDownload = customtkinter.CTkButton(master=frameBtn, text='Get Details', command=getDetails,
                                          fg_color='#880ED4',height=40)
videoDownload = customtkinter.CTkButton(master=frameBtn, text='Video', command=startDownload,
                                        fg_color='green',height=40)
audioDownload = customtkinter.CTkButton(master=frameBtn, text='Audio', command=audiosDownload,
                                        fg_color='red',height=40)


detailsDownload.pack(pady=20, side='left', padx=10)
videoDownload.pack(pady=20, side='left', padx=10)
audioDownload.pack(pady=20, side='left', padx=10)
frameBtn.pack(pady=20, padx=10)

finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack(pady=20)

app.resizable(width=False, height=False)
app.mainloop()
