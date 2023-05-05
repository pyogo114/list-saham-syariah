from pytube import YouTube


url = YouTube(str("https://www.youtube.com/watch?v=OuSIF7UYiJU")) #This captures the link(url) and locates it from YouTube.
url.streams.filter(file_extension='mp4').first().download() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.

