
from pytube import YouTube



#url = YouTube(str("https://www.youtube.com/watch?v=Al0PhuFnKTM")) #This captures the link(url) and locates it from YouTube.
url = YouTube(str("https://noodlemagazine.com/watch/-158139736_456243986")) #This captures the link(url) and locates it from YouTube.


video = url.streams.first() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
#video = url.streams.filter(file_extension='mp4')
video.download() # This is the method with the instruction to download the video.

# https://pytube.io/en/latest/user/cli.html