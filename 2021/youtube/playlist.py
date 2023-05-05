from pytube import YouTube,Playlist

URLVIDEOPERTAMA = "https://www.youtube.com/watch?v=7Xxockv1JyE&list=PLQ02IYL5pmhHLxCC7SexvhCsIFviGjfmU"

p = Playlist(URLVIDEOPERTAMA)

print(f'Downloading: {p.title}')

for video in p.videos:
    #video.streams.first().download()
    #video.streams.filter(file_extension='mp4').first().download()
    video.streams.filter(only_audio=True).first().download()
  
    