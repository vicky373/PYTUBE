import tkinter
from customtkinter import filedialog 
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink=Link.get()
        ytObject=YouTube(ytLink,on_progress_callback=on_progress)
        streams = set()

        for stream in ytObject.streams.filter(type="video"):  # Only look for video streams to avoid None values
              streams.add(stream.resolution)
        print(streams)
        
        print(ytObject.streams)
        # for stream in ytObject.streams.filter(resolution="2160p"):
        #     print(stream)
        video=ytObject.streams.get_highest_resolution()
        title.configure(text=video.title,text_color="white")
        finishlabel.configure(text="")
        video.download(output_path=folder_path.get())
        finishlabel.configure(text="Downloaded Video")
        # video=ytObject.streams.get_highest_resolution()
        # res = ytObject.streams.itag_index()
        # print(res)
        # if int(res.replace("p", "")) > 1080:
        #     res = 1080
        # video=ytObject.streams.get_by_resolution(res)        
    except:
        finishlabel.configure(text="Downloaded Error",text_color="red")
        
def on_progress(stream,chunk,bytes_remaining):
    total_size=stream.filesize
    bytes_downloaded=total_size - bytes_remaining
    percentage_completed=bytes_downloaded / total_size * 100  
    per=str(int(percentage_completed))
    progper.configure(text=per+"%")
    progper.update()
    
    progressBar.set(float(percentage_completed)/100)


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

def switch_event():
    if switch_var.get() == "on":
        customtkinter.set_appearance_mode("Light")
        customtkinter.set_default_color_theme("blue")
        switch_text_var.set("Light Mode")
        
    else:
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("green")
        switch_text_var.set("Dark Mode")
        

        
        
       
def browse_button():
    filename = filedialog.askdirectory()
    folder_path.set(filename)

#Our application frame

app = customtkinter.CTk()
app.geometry("1080x720")
app.title("Youtube Video Downlaoder")

# appearance mode switching light/Dark
switch_var = customtkinter.StringVar(value="off")
switch_text_var=customtkinter.StringVar(value="Dark Mode")
switch = customtkinter.CTkSwitch(app,command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off",button_color="black",textvariable=switch_text_var)
switch.pack(padx=40,pady=40)

#Adding UI elemets

title=customtkinter.CTkLabel(app,text="Insert Youtube URL")
title.pack(padx=10,pady=10)

url_variable=tkinter.StringVar()
Link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_variable,placeholder_text="Paste URL here",placeholder_text_color="white")
Link.pack()

#finished downloading
finishlabel=customtkinter.CTkLabel(app,text="")
finishlabel.pack()

# Resolution Options
option_list=["720p","480p","360p"]
combobox_var = customtkinter.StringVar()
combobox = customtkinter.CTkComboBox(app, values=option_list,variable=combobox_var)
combobox.pack(padx=80,pady=10)

#progress percentage
progper=customtkinter.CTkLabel(app,text="0%")
progper.pack()
progressBar=customtkinter.CTkProgressBar(app,width=600)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

#file browse button functionality
folder_path=customtkinter.StringVar()
file_path=customtkinter.CTkLabel(app,textvariable=folder_path)
browse_button=customtkinter.CTkButton(app,text="Browse",command=browse_button)
browse_button.pack(padx=10,pady=10)
file_path.pack(padx=10,pady=10)
#download button
download = customtkinter.CTkButton(app,
                                 text="Download",
                                 command=startDownload,
                                 width=200,
                                 height=32,
                                 border_width=0,
                                 corner_radius=32)
download.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
download.pack(padx=10,pady=10)

app.mainloop()