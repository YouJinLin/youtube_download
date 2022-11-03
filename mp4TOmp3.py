from moviepy.editor import *
video = VideoFileClip(r'D:\YouTube\A Rock Can Be A Star.mp4')
try:
    video.audio.write_audiofile(r'D:\YouTube\A Rock Can Be A Star.mp3')
except:
    print('Error')