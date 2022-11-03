from pytube import YouTube
import tkinter as tk
import os

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
            yt.streams.filter(progressive=True,subtype="mp4",res="360p").first().download(path.get())
            resulttxt.set("360p下載完成") 
        except:
            resulttxt.set("下載失敗")   
        
 
    elif(choice.get()=="720p,mp4"):
        try:
            yt=YouTube(website.get())
            yt.streams.filter(progressive=True,subtype="mp4",res="720p").first().download(path.get())
            resulttxt.set("720p下載完成")
        except:
            resulttxt.set("下載失敗") 
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
item1=tk.Radiobutton(frame3,text="360p,mp4",value="360p,mp4",variable=choice,foreground="black",font=("新細明體",16))
item1.pack()
item2=tk.Radiobutton(frame3,text="720p,mp4",value="720p,mp4",variable=choice,foreground="black",font=("新細明體",16))
item2.pack()
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
ui.mainloop()