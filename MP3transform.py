from pytube import YouTube
import tkinter as tk
import os
import moviepy.editor as edit

def transform(title):  #mp4 轉換mp3  
    video = edit.VideoFileClip(title)
    Newtitle = title.split(sep=".")[0]
    try:
        video.audio.write_audiofile(f'{Newtitle}.mp3')
        transresult.set("轉換完成")
        print("轉換成功")
    except:
        transresult.set("轉換失敗")
        print("轉換失敗")

def check_website():
    if(len(website.get())==0):
        resulttxt.set("請輸入網址")
    else:
        check_path()
def check_path():
    if(len(path.get())==0):
        path.set(r"D:\YouTube")
    elif(not os.path.isdir(path.get())):
        os.mkdir(path.get())
    download()

def download():    
    if(choice.get()=="360p,mp4"):  
        try:
            yt=YouTube(website.get())
            videoTitle = yt.streams.filter(progressive=True,subtype="mp4",res="360p").first().download(path.get())
            resulttxt.set("下載完成") 
            transform(videoTitle)
            print(str(videoTitle))
        except:
            resulttxt.set("下載失敗")   
            print(videoTitle.split(sep=".")[0])
        
#建立UI
ui=tk.Tk()
ui.geometry("500x500")
ui.title("Youtube下載器")
#網址輸入
frame1=tk.Frame(ui)
frame1.pack()
label1=tk.Label(frame1,text="下載網址:",foreground="blue",font=("新細明體",16),)
website=tk.StringVar()
text1=tk.Entry(frame1,textvariable=website)
label1.grid(row=0,column=0,pady=30,sticky="s")
text1.grid(row=0,column=1,pady=30,sticky="s")
#儲存位置
frame2=tk.Frame(ui) 
frame2.pack()
label2=tk.Label(frame2,text="儲存位置:",foreground="blue",font=("新細明體",16))
path=tk.StringVar()
text2=tk.Entry(frame2,textvariable=path)
label2.grid(row=0,column=0,pady=40)
text2.grid(row=0,column=1,pady=40)
#選擇格式
frame3=tk.Frame(ui)
frame3.pack(pady=30)
choice=tk.StringVar()
item1=tk.Radiobutton(frame3,text="mp4 download",value="360p,mp4",variable=choice,foreground="black",font=("新細明體",16))
item1.pack()
item1.select()
#下載鈕
frame4=tk.Frame(ui) 
frame4.pack()
button1=tk.Button(frame3,text="下載影片",font=("新細明體",16),command=check_website,foreground="purple")
button1.pack(pady=40)
#結果顯示
frame5=tk.Frame(ui) 
frame5.pack()
resulttxt=tk.StringVar()
result=tk.Label(frame5,foreground="red",font=("新細明體",16),textvariable=resulttxt)
result.pack()
transresult = tk.StringVar()
trans = tk.Label(frame5, foreground="red", font=("新細明體",16), textvariable=transresult)
trans.pack()
ui.mainloop()